import argparse
import grpc
import json

from aptos_indexer_protos.aptos.indexer.v1 import raw_data_pb2, raw_data_pb2_grpc
from aptos_indexer_protos.aptos.transaction.v1 import transaction_pb2
from utils.config import Config, NFTMarketplaceV2Config
from utils.models.general_models import Base
from utils.session import Session
from utils.metrics import PROCESSED_TRANSACTIONS_COUNTER
from sqlalchemy import DDL, create_engine
from sqlalchemy import event
from typing import Iterator, List, Optional
from prometheus_client.twisted import MetricsResource
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import threading
import sys
from utils.transactions_processor import TransactionsProcessor, ProcessingResult
from time import perf_counter, sleep
import traceback
from utils.processor_name import ProcessorName
from processors.example_event_processor.processor import ExampleEventProcessor
from processors.nft_orderbooks.nft_marketplace_processor import NFTMarketplaceProcesser
from processors.nft_marketplace_v2.processor import NFTMarketplaceV2Processor
from processors.coin_flip.processor import CoinFlipProcessor
from processors.aptos_ambassador_token.processor import AptosAmbassadorTokenProcessor
import asyncio
import logging
import queue
import os

INDEXER_GRPC_BLOB_STORAGE_SIZE = 1000
INDEXER_GRPC_MIN_SEC_BETWEEN_GRPC_RECONNECTS = 60
# How large the fetcher queue should be
FETCHER_QUEUE_SIZE = 50
# We will try to reconnect to GRPC once every X seconds if we get disconnected, before crashing
# We define short connection issue as < 10 seconds so adding a bit of a buffer here
MIN_SEC_BETWEEN_GRPC_RECONNECTS = 15
# We will try to reconnect to GRPC 5 times in case upstream connection is being updated
RECONNECTION_MAX_RETRIES = 5


def get_grpc_stream(
    indexer_grpc_data_service_address: str,
    indexer_grpc_data_stream_api_key: str,
    indexer_grpc_http2_ping_interval_in_secs: int,
    indexer_grpc_http2_ping_timeout_in_secs: int,
    starting_version: int,
    ending_version: Optional[int],
    processor_name: str,
) -> Iterator[raw_data_pb2.TransactionsResponse]:
    logging.info(
        json.dumps(
            {
                "processor_name": processor_name,
                "stream_address": indexer_grpc_data_service_address,
                "message": "[Parser] Setting up rpc channel",
            }
        ),
    )

    metadata = (
        ("authorization", "Bearer " + indexer_grpc_data_stream_api_key),
        ("x-aptos-request-name", processor_name),
    )
    options = [
        ("grpc.max_receive_message_length", -1),
        (
            "grpc.keepalive_time_ms",
            indexer_grpc_http2_ping_interval_in_secs * 1000,
        ),
        (
            "grpc.keepalive_timeout_ms",
            indexer_grpc_http2_ping_timeout_in_secs * 1000,
        ),
    ]

    channel = grpc.secure_channel(
        indexer_grpc_data_service_address,
        options=options,
        credentials=grpc.ssl_channel_credentials(),
    )
    transactions_count = (
        ending_version - starting_version + 1 if ending_version else None
    )

    logging.info(
        json.dumps(
            {
                "processor_name": processor_name,
                "stream_address": indexer_grpc_data_service_address,
                "starting_version": starting_version,
                "ending_version": ending_version,
                "count": transactions_count,
                "message": "[Parser] Setting up stream",
            }
        ),
    )

    try:
        stub = raw_data_pb2_grpc.RawDataStub(channel)
        request = raw_data_pb2.GetTransactionsRequest(
            starting_version=starting_version, transactions_count=transactions_count
        )
        responses = stub.GetTransactions(request, metadata=metadata)
        return iter(responses)
    except Exception as e:
        logging.exception(
            json.dumps(
                {
                    "message": "[Parser] Failed to get grpc response. Is the server running?",
                }
            ),
        )
        os._exit(1)


# Gets a batch of transactions from the stream. Batch size is set in the grpc server.
# The number of batches depends on our config
# There could be several special scenarios:
# 1. If we lose the connection, we will try reconnecting X times within Y seconds before crashing.
# 2. If we specified an end version and we hit that, we will stop fetching, but we will make sure that
# all existing transactions are processed
def producer(
    q: queue.Queue,
    indexer_grpc_data_service_address: str,
    indexer_grpc_data_stream_api_key: str,
    indexer_grpc_http2_ping_interval: int,
    indexer_grpc_http2_ping_timeout: int,
    starting_version: int,
    ending_version: Optional[int],
    processor_name: str,
    batch_start_version: int,
):
    last_insertion_time = perf_counter()
    next_version_to_fetch = batch_start_version
    last_reconnection_time = None
    reconnection_retries = 0
    response_stream = get_grpc_stream(
        indexer_grpc_data_service_address,
        indexer_grpc_data_stream_api_key,
        indexer_grpc_http2_ping_interval,
        indexer_grpc_http2_ping_timeout,
        starting_version,
        ending_version,
        processor_name,
    )

    logging.info(
        json.dumps(
            {
                "processor_name": processor_name,
                "stream_address": indexer_grpc_data_service_address,
                "starting_version": starting_version,
                "ending_version": ending_version,
                "message": "[Parser] Successfully connected to GRPC endpoint",
            }
        ),
    )

    while True:
        is_success = False
        try:
            response = next(response_stream)
            reconnection_retries = 0
            batch_start_version = response.transactions[0].version
            batch_end_version = response.transactions[-1].version
            next_version_to_fetch = batch_end_version + 1

            chain_id = response.chain_id
            assert chain_id is not None, "[Parser] Chain Id doesn't exist"
            q.put((chain_id, response.transactions))

            logging.info(
                json.dumps(
                    {
                        "processor_name": processor_name,
                        "start_version": str(batch_start_version),
                        "end_version": str(batch_end_version),
                        "channel_size": q.qsize(),
                        "channel_recv_latency_in_secs": str(
                            format(perf_counter() - last_insertion_time, ".8f")
                        ),
                        "message": "[Parser] Received chunk of transactions",
                    }
                ),
            )
            last_insertion_time = perf_counter()
            is_success = True
        except StopIteration:
            logging.info(
                json.dumps(
                    {
                        "processor_name": processor_name,
                        "stream_address": indexer_grpc_data_service_address,
                        "message": "[Parser] Stream ended",
                    }
                ),
            )
        except Exception as e:
            logging.exception(
                json.dumps(
                    {
                        "processor_name": processor_name,
                        "stream_address": indexer_grpc_data_service_address,
                        "message": "[Parser] Error receiving datastream response",
                    },
                    indent=4,
                )
            )

        # Check if we're at the end of the stream
        reached_ending_version = (
            next_version_to_fetch > ending_version if ending_version else False
        )
        if reached_ending_version:
            logging.info(
                json.dumps(
                    {
                        "processor_name": processor_name,
                        "stream_address": indexer_grpc_data_service_address,
                        "ending_version": ending_version,
                        "next_version_to_fetch": next_version_to_fetch,
                        "message": "[Parser] Reached ending version",
                    }
                ),
            )
            # Wait for the fetched transactions to finish processing before closing the channel
            while True:
                logging.info(
                    json.dumps(
                        {
                            "processor_name": processor_name,
                            "channel_size": q.qsize(),
                            "message": "[Parser] Waiting for channel to be empty",
                        }
                    ),
                )
                if q.qsize() == 0:
                    break
            logging.info(
                json.dumps(
                    {
                        "message": "[Parser] The stream is ended",
                    }
                ),
            )
            break
        else:
            # The rest is to see if we need to reconnect
            if is_success:
                continue

            if last_reconnection_time:
                elapsed_secs = perf_counter() - last_reconnection_time
                if (
                    reconnection_retries >= RECONNECTION_MAX_RETRIES
                    and elapsed_secs < MIN_SEC_BETWEEN_GRPC_RECONNECTS
                ):
                    logging.warn(
                        json.dumps(
                            {
                                "processor_name": processor_name,
                                "stream_address": indexer_grpc_data_service_address,
                                "seconds_since_last_retry": str(elapsed_secs),
                                "message": "[Parser] Recently reconnected. Will not retry.",
                            }
                        ),
                    )
                    os._exit(1)
            reconnection_retries += 1
            last_reconnection_time = perf_counter()
            logging.info(
                json.dumps(
                    {
                        "processor_name": processor_name,
                        "stream_address": indexer_grpc_data_service_address,
                        "starting_version": next_version_to_fetch,
                        "ending_version": ending_version,
                        "reconnection_retries": reconnection_retries,
                        "message": "[Parser] Reconnecting to GRPC.",
                    }
                ),
            )
            response_stream = get_grpc_stream(
                indexer_grpc_data_service_address,
                indexer_grpc_data_stream_api_key,
                indexer_grpc_http2_ping_interval,
                indexer_grpc_http2_ping_timeout,
                next_version_to_fetch,
                ending_version,
                processor_name,
            )


# This is the consumer side of the channel. These are the major states:
# 1. We're backfilling so we should expect many concurrent threads to process transactions
# 2. We're caught up so we should expect a single thread to process transactions
# 3. We have received either an empty batch or a batch with a gap. We should panic.
# 4. We have not received anything in X seconds, we should panic.
# 5. If it's the wrong chain, panic.
def consumer(
    q: queue.Queue,
    producer_thread: threading.Thread,
    indexer_grpc_data_stream_endpoint: str,
    processor: TransactionsProcessor,
    num_concurrent_processing_tasks: int,
    starting_version: int,
    processor_name: str,
):
    asyncio.run(
        consumer_impl(
            q,
            producer_thread,
            indexer_grpc_data_stream_endpoint,
            processor,
            num_concurrent_processing_tasks,
            starting_version,
            processor_name,
        )
    )


async def consumer_impl(
    q: queue.Queue,
    producer_thread: threading.Thread,
    indexer_grpc_data_stream_endpoint: str,
    processor: TransactionsProcessor,
    num_concurrent_processing_tasks: int,
    starting_version: int,
    processor_name: str,
):
    chain_id = None
    batch_start_version = starting_version

    while True:
        tps_start_time = perf_counter()

        # Check if producer task is done
        if not producer_thread.is_alive():
            logging.info(
                json.dumps(
                    {
                        "processor_name": processor_name,
                        "message": "[Parser] Channel closed; stream ended.",
                    }
                ),
            )
            os._exit(0)

        # Fetch transaction batches from channel to process
        transaction_batches = []
        last_fetched_version = batch_start_version - 1
        for task_index in range(num_concurrent_processing_tasks):
            if task_index == 0:
                # If we're the first task, we should wait until we get data.
                chain_id, transactions = q.get()
            else:
                # If we're not the first task, we should poll to see if we get any data.
                try:
                    chain_id, transactions = q.get_nowait()
                except queue.Empty:
                    # Channel is empty and send is not dropped which we definitely expect. Wait for a bit and continue polling.
                    continue

            # TODO: Check chain_id saved in DB

            current_fetched_version = transactions[0].version
            if last_fetched_version + 1 != current_fetched_version:
                logging.warn(
                    json.dumps(
                        {
                            "processor_name": processor_name,
                            "last_fetched_version": last_fetched_version,
                            "current_fetched_version": current_fetched_version,
                            "message": "[Parser] Received batch with gap from GRPC stream",
                        }
                    )
                )
                os._exit(1)
            last_fetched_version = transactions[-1].version
            transaction_batches.append(transactions)

        processor_threads = []
        for transactions in transaction_batches:
            thread = IndexerProcessorServer.WorkerThread(processor, transactions)
            processor_threads.append(thread)
            thread.start()

        for thread in processor_threads:
            thread.join()

        processing_time = perf_counter()
        task_count = len(processor_threads)
        processed_versions: List[ProcessingResult] = []
        for thread in processor_threads:
            if thread.exception:
                logging.warn(
                    json.dumps(
                        {
                            "processor_name": processor_name,
                            "message": "[Parser] Error processing transaction batch",
                        }
                    )
                )
                os._exit(1)

            processed_versions.append(thread.processing_result)

        logging.info(
            json.dumps(
                {
                    "processor_name": processor_name,
                    "task_count": task_count,
                    "processing_duration": str(
                        format(perf_counter() - processing_time, ".8f")
                    ),
                    "message": "[Parser] Finished processing transaction batches",
                }
            )
        )

        # Make sure there are no gaps and advance states
        prev_start = None
        prev_end = None
        for result in processed_versions:
            if prev_start is None or prev_end is None:
                prev_start = result.start_version
                prev_end = result.end_version
            else:
                if prev_end + 1 != result.start_version:
                    logging.warn(
                        json.dumps(
                            {
                                "processor_name": processor_name,
                                "stream_address": indexer_grpc_data_stream_endpoint,
                                "processed_versions": processed_versions,
                                "message": "[Parser] Gaps in processing stream",
                            }
                        )
                    )
                    os._exit(1)
                prev_start = result.start_version
                prev_end = result.end_version

        processed_start_version = processed_versions[0].start_version
        processed_end_version = processed_versions[-1].end_version
        batch_start_version = processed_end_version + 1

        processor.update_last_processed_version(processed_end_version)
        PROCESSED_TRANSACTIONS_COUNTER.inc(
            processed_end_version - processed_start_version + 1
        )

        tps_end_time = perf_counter()

        logging.info(
            json.dumps(
                {
                    "processor_name": processor.name(),
                    "start_version": str(processed_start_version),
                    "end_version": str(processed_end_version),
                    "batch_size": str(
                        processed_end_version - processed_start_version + 1
                    ),
                    "tps": f"{(processed_end_version - processed_start_version + 1) / (tps_end_time - tps_start_time)}",
                    "message": f"[Parser] Processed transactions",
                }
            ),
        )


class IndexerProcessorServer:
    config: Config
    num_concurrent_processing_tasks: int

    def __init__(self, config: Config):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "fields": %(message)s}'
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.config = config
        logging.info(
            json.dumps(
                {
                    "processor_name": self.config.server_config.processor_config.type,
                    "message": "[Parser] Kicking off",
                }
            )
        )

        # Instantiate the correct processor based on config
        processor_config = self.config.server_config.processor_config
        match processor_config.type:
            case ProcessorName.EXAMPLE_EVENT_PROCESSOR.value:
                self.processor = ExampleEventProcessor()
            case ProcessorName.NFT_MARKETPLACE_V1_PROCESSOR.value:
                self.processor = NFTMarketplaceProcesser()
            case ProcessorName.NFT_MARKETPLACE_V2_PROCESSOR.value:
                assert isinstance(processor_config, NFTMarketplaceV2Config)
                self.processor = NFTMarketplaceV2Processor(processor_config)
            case ProcessorName.COIN_FLIP.value:
                self.processor = CoinFlipProcessor()
            case ProcessorName.EXAMPLE_AMBASSADOR_TOKEN_PROCESSOR.value:
                self.processor = AptosAmbassadorTokenProcessor()
            case _:
                raise Exception(
                    "Invalid processor name"
                    "\n[ERROR]: The specified processor name was invalid or not found.\n"
                    "         - If you are using a custom processor, make sure to add it to the ProcessorName enum in utils/processor_name.py.\n"
                    "         - Ensure the IndexerProcessorServer constructor in utils/worker.py uses the new enum value.\n"
                )

        # TODO: Move this to a config
        self.num_concurrent_processing_tasks = 10

    class WorkerThread(
        threading.Thread,
    ):
        processing_result: ProcessingResult
        exception: Exception | None

        def __init__(
            self,
            processor: TransactionsProcessor,
            transactions: List[transaction_pb2.Transaction],
        ):
            threading.Thread.__init__(self)
            self.processor = processor
            self.transactions = transactions
            self.processing_result = ProcessingResult(
                transactions[0].version, transactions[-1].version
            )
            self.exception = None

        def run(self):
            start_version = self.transactions[0].version
            end_version = self.transactions[-1].version

            try:
                self.processing_result = self.processor.process_transactions(
                    self.transactions, start_version, end_version
                )

            except Exception as e:
                self.exception = e

    def run(self):
        processor_name = self.config.server_config.processor_config.type
        indexer_grpc_address = (
            self.config.server_config.indexer_grpc_data_service_address
        )

        # Run DB migrations
        logging.info(
            json.dumps(
                {
                    "processor_name": self.processor.name(),
                    "message": "[Parser] Initializing DB tables",
                }
            ),
        )
        self.init_db_tables(self.processor.schema())
        logging.info(
            json.dumps(
                {
                    "processor_name": self.processor.name(),
                    "message": "[Parser] DB tables initialized",
                }
            )
        )

        self.start_health_and_monitoring_ports()

        # Get starting version from DB
        starting_version = self.config.get_starting_version(self.processor.name())
        ending_version = self.config.server_config.ending_version

        # Create a transaction fetcher thread that will continuously fetch transactions from the GRPC stream
        # and write into a channel. Each item is of type (chain_id, vec of transactions)
        logging.info(
            json.dumps(
                {
                    "processor_name": processor_name,
                    "stream_address": self.config.server_config.indexer_grpc_data_service_address,
                    "start_version": starting_version,
                    "message": "[Parser] Starting fetcher task",
                }
            )
        )
        q = queue.Queue(FETCHER_QUEUE_SIZE)
        producer_thread = threading.Thread(
            target=producer,
            daemon=True,
            args=(
                q,
                indexer_grpc_address,
                self.config.server_config.auth_token,
                self.config.server_config.indexer_grpc_http2_ping_interval_in_secs,
                self.config.server_config.indexer_grpc_http2_ping_timeout_in_secs,
                starting_version,
                ending_version,
                processor_name,
                starting_version,
            ),
        )
        producer_thread.start()

        consumer_thread = threading.Thread(
            target=consumer,
            daemon=True,
            args=(
                q,
                producer_thread,
                indexer_grpc_address,
                self.processor,
                self.num_concurrent_processing_tasks,
                starting_version,
                processor_name,
            ),
        )
        consumer_thread.start()

        producer_thread.join()
        consumer_thread.join()

    def init_db_tables(self, schema_name: str) -> None:
        engine = create_engine(self.config.server_config.postgres_connection_string)
        engine = engine.execution_options(
            schema_translate_map={"per_schema": schema_name}
        )
        Session.configure(bind=engine)
        Base.metadata.create_all(engine, checkfirst=True)

    def start_health_and_monitoring_ports(self) -> None:
        # Start the health + metrics server.
        def start_health_server() -> None:
            # The kubelet uses liveness probes to know when to restart a container. In cases where the
            # container is crashing or unresponsive, the kubelet receives timeout or error responses, and then
            # restarts the container. It polls every 10 seconds by default.
            root = Resource()
            root.putChild(b"metrics", MetricsResource())  # type: ignore

            class ServerOk(Resource):
                isLeaf = True

                def render_GET(self, request):
                    return b"ok"

            root.putChild(b"", ServerOk())  # type: ignore
            factory = Site(root)
            reactor.listenTCP(self.config.health_check_port, factory)  # type: ignore
            reactor.run(installSignalHandlers=False)  # type: ignore

        t = threading.Thread(target=start_health_server, daemon=True)
        # TODO: Handles the exit signal and gracefully shutdown the server.
        t.start()


@event.listens_for(Base.metadata, "before_create")
def create_schemas(target, connection, **kw):
    schemas = set()
    for table in target.tables.values():
        if table.schema is not None:
            schemas.add(table.schema)
    for schema in schemas:
        connection.execute(DDL("CREATE SCHEMA IF NOT EXISTS %s" % schema))


@event.listens_for(Base.metadata, "after_drop")
def drop_schemas(target, connection, **kw):
    schemas = set()
    for table in target.tables.values():
        if table.schema is not None:
            schemas.add(table.schema)
    for schema in schemas:
        connection.execute(DDL("DROP SCHEMA IF EXISTS %s" % schema))
