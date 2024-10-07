import time
from dapr.clients import DaprClient
import grpc_types.service_pb2 as service_pb2
import grpc_types.service_pb2_grpc as service_pb2_grpc
# with DaprClient() as d:
#     # Create a protobuf request message
#     req_data = service_pb2.JsonMethodRequest(
#         json_data='{"id": 1, "message": "hello world"}'
#     )

#     while True:
#         # Serialize the request message
#         serialized_data = req_data.SerializeToString()

#         # Invoke the method using the serialized protobuf data
#         resp = d.invoke_method(
#             'invoke-receiver',
#             'json-method',
#             data=serialized_data,
#             content_type="application/protobuf"
#         )

#         # Deserialize the response using protobuf
#         response_message = service_pb2.JsonMethodResponse()
#         response_message.ParseFromString(resp.data)

#         # Print the deserialized response
#         print(response_message.received, flush=True)
#         print(response_message.message, flush=True)

#         time.sleep(2)



import grpc
import time
import logging
import os
import sys
# import grpc_types.service_pb2 as service_pb2
# import grpc_types.service_pb2_grpc as service_pb2_grpc


def build_grpc_channel(native_grpc_port, dapr_grpc_port, command_line_port = None):
    native_grpc_host = "contoso.local" #to match the ssl certificate CN
    if dapr_grpc_port == 0:
        port = command_line_port if command_line_port != None else native_grpc_port
    else:
        port = dapr_grpc_port
    if (port != native_grpc_port): # running in dapr
        grpc_channel = grpc.insecure_channel(f"localhost:{port}")
        logging.info(f'Connecting to localhost:{port}')
    else:
        with open('certs\server.crt', 'rb') as f:
            channel_credentials = grpc.ssl_channel_credentials(f.read())
        grpc_channel = grpc.secure_channel(f"{native_grpc_host}:{port}", channel_credentials) #grpc.local_channel_credentials() also works in dev.
        logging.info(f'Connecting to secure {native_grpc_host}:{port}')
    return grpc_channel

def run():
    # Set up a connection to the server.
    command_line_port = sys.argv[2] if len(sys.argv) > 2 else None
    dapr_grpc_port = os.getenv('DAPR_GRPC_PORT', 0)
    # channel = grpc.insecure_channel('localhost:50007')

    # Create a context with a timeout and add metadata
    metadata = (('dapr-app-id', 'invoke-receiver'),)
    # context = grpc.metadata_call_credentials(metadata)

    try:
        with build_grpc_channel(0, dapr_grpc_port, command_line_port) as channel:
            stub = service_pb2_grpc.ReceiverServiceStub(channel)
            # Send a request to the server
            response = stub.MyMethod(
                service_pb2.MyMethodRequest(text='Darth Tyrannus'),
                # timeout=2,
                metadata=metadata
            )
            print(f"Greeting: {response.message}")
    except grpc.RpcError as e:
        print(f"Could not greet: {e}")

if __name__ == '__main__':
    run()