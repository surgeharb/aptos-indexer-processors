from grpc_parser import parse
from aptos.datastream.v1 import datastream_pb2_grpc

import grpc
from aptos.datastream.v1 import datastream_pb2
from aptos.transaction.testing1.v1 import transaction_pb2

from google import auth as google_auth
from google.auth.transport import grpc as google_auth_transport_grpc
from google.auth.transport import requests as google_auth_transport_requests

import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

metadata = (("x-aptos-data-authorization", config["x-aptos-data-authorization"]),)
options = [('grpc.max_receive_message_length', -1)]

with grpc.insecure_channel(config["indexer-endpoint"], options=options) as channel:
    stub = datastream_pb2_grpc.IndexerStreamStub(channel)
    current_transaction_version = config["starting-version"]

    for response in stub.RawDatastream(datastream_pb2.RawDatastreamRequest(starting_version=config["starting-version"]), metadata=metadata):
        chain_id = response.chain_id

        if chain_id != config["chain-id"]:
            raise Exception("Chain ID mismatch. Expected chain ID is: " + str(config["chain-id"]) + ", but received chain ID is: " + str(chain_id))
        
        transactions_output = response.data
        for transaction_output in transactions_output.transactions:
            # Decode transaction data
            transaction = transaction_pb2.Transaction()
            transaction.ParseFromString(transaction_output.encoded_proto_data)

            transaction_version = transaction.version
            if transaction_version != current_transaction_version:
                raise Exception("Transaction version mismatch. Expected transaction version is: " + str(current_transaction_version) + ", but received transaction version is: " + str(transaction_version))

            current_transaction_version += 1
            parsed_transaction = parse(transaction)