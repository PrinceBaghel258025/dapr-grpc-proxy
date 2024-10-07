# Executing Remote RPC Method Using Dapr gRPC Proxy

This documentation outlines how to execute a remote RPC method using the Dapr gRPC proxy, focusing on the implementation in `invoke-caller.py` and how it interacts with `invoke-receiver.py`. We'll also cover how to start both the invoker and receiver services using Dapr.

## Overview of `invoke-caller.py`

The `invoke-caller.py` script demonstrates how to use Dapr's service invocation to call gRPC methods on a remote service. Here's a breakdown of its key components:

1. **Imports and Setup**
   The script imports necessary modules, including gRPC and Dapr-related libraries.

2. **Channel Building Function**
   ```python
   def build_grpc_channel(native_grpc_port, dapr_grpc_port, command_line_port = None):
       # ... (function implementation)
   ```
   This function creates a gRPC channel based on the environment (Dapr or native gRPC).

3. **Main Execution Function**
   ```python
   def run():
       # ... (function implementation)
   ```
   This function orchestrates the gRPC call process.

## How `invoke-caller.py` Works

1. **Environment Setup**
   - The script checks for a Dapr environment by looking for the `DAPR_GRPC_PORT` environment variable.
   - It also accepts a command-line port argument for flexibility.

2. **Channel Creation**
   - A gRPC channel is created using the `build_grpc_channel` function.
   - If running in Dapr, it creates an insecure channel to `localhost` on the Dapr-assigned port.
   - For non-Dapr environments, it sets up a secure channel with SSL credentials.

3. **Service Invocation**
   - A gRPC stub is created for the `ReceiverService`.
   - The script adds Dapr-specific metadata to the call:
     ```python
     metadata = (('dapr-app-id', 'invoke-receiver'),)
     ```
   - It then calls the `MyMethod` on the remote service:
     ```python
     response = stub.MyMethod(
         service_pb2.MyMethodRequest(text='Darth Tyrannus'),
         metadata=metadata
     )
     ```

4. **Error Handling**
   - The script includes basic error handling for gRPC exceptions.

## How `invoke-receiver.py` Handles the Request

The `invoke-receiver.py` script sets up a gRPC server that handles incoming requests. Here's how it works:

1. **Service Definition**
   ```python
   class ReceiverService(service_pb2_grpc.ReceiverServiceServicer):
       def MyMethod(self, request, context):
           # ... (method implementation)
       
       def JsonMethod(self, request, context):
           # ... (method implementation)
   ```
   This class defines the methods that can be called remotely.

2. **Request Handling**
   - The `MyMethod` prints the received metadata and text, then returns a simple response.
   - The `JsonMethod` processes JSON data and interacts with Dapr's state store.

3. **Server Setup**
   ```python
   def serve():
       server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
       service_pb2_grpc.add_ReceiverServiceServicer_to_server(ReceiverService(), server)
       server.add_insecure_port('[::]:50051')
       server.start()
       server.wait_for_termination()
   ```
   This function sets up and starts the gRPC server on port 50051.

## Starting the Services with Dapr

The `dapr1.yaml` and `dapr2.yaml` files define how to start the receiver and invoker services using Dapr.

### Receiver Service (`dapr1.yaml`)



