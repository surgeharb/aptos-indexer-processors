# Aptos Indexer Client Guide
This guide will get you started with creating an Aptos indexer with custom parsing. We have several endpoints that provided a streaming RPC of transaction data.

## GRPC Data Stream Endpoints
* devnet: https://grpc.devnet.aptoslabs.com:443

* testnet: https://grpc.testnet.aptoslabs.com:443

* mainnet: https://grpc.mainnet.aptoslabs.com:443

## Request
 - `config.yaml`
   - `chain_id`: ID of the chain used for validation purposes.
   - `grpc_data_stream_endpoint`: Replace with the grpc data stream endpoints for mainnet, devnet, testnet, or previewnet.
   - `grpc_data_stream_api_key`: Replace `YOUR_TOKEN` with your auth token.
   - `db_connection_uri`: The DB connection used to write the processed data
   - (optional) `starting-version`
     - If `starting-version` is set, the processor will begin indexing from transaction version = `starting_version`.
     - To auto restart the client in case of an error, you can cache the latest processed transaction version. In the example, the processor restarts from cached transaction version that is stored in a table, and if neither `starting_version` nor cached version are set, the processor defaults starting version to 0.

## Response
- The response is a stream of `RawDatastreamResponse` objects.
- For each supported language, there is an `aptos` folder which contains the auto-generate protobuf files in that language. You can check out the files to see the stream response format and figure out how to parse the response.

## [Aptos Indexer GRPC Release Notes](https://github.com/aptos-labs/aptos-core/blob/main/ecosystem/indexer-grpc/release_notes.md)


## Dev Guide

### Development
If you update the proto definitions in `proto/`, you can regenerate them for all languages by running this script:
```
./scripts/build_protos.sh
```

Make sure you have the following deps installed:
```bash
# Install buf
brew install bufbuild/buf/buf

# For generating Rust code
cargo install protoc-gen-prost
cargo install protoc-gen-prost-serde
cargo install protoc-gen-prost-crate
cargo install protoc-gen-tonic

# For generating TS code
pnpm install -g protoc-gen-ts@0.8.7

# For generating Python code
cd python/aptos-indexer-protos
poetry install
```
