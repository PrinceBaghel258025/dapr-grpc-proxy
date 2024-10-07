# from dapr.ext.grpc import App, InvokeMethodRequest, InvokeMethodResponse
# import json
# from dapr.clients import DaprClient
# import grpc_types.service_pb2 as service_pb2
# # import grpc_types.service_pb2_grpc as service_pb2_grpc

# app = App()

# @app.method(name='my-method')
# def mymethod(request: InvokeMethodRequest) -> InvokeMethodResponse:
#     # Deserialize the request using protobuf
#     my_method_request = service_pb2.MyMethodRequest()
#     my_method_request.ParseFromString(request.data)
    
#     print(my_method_request.metadata, flush=True)
#     print(my_method_request.text, flush=True)

#     # Create a response using protobuf
#     response = service_pb2.MyMethodResponse(message='INVOKE_RECEIVED')
#     return InvokeMethodResponse(response.SerializeToString(), "application/protobuf")

# @app.method(name='json-method')
# def json_method(request: InvokeMethodRequest) -> InvokeMethodResponse:
#     # Deserialize the request using protobuf
#     json_method_request = service_pb2.JsonMethodRequest()
#     json_method_request.ParseFromString(request.data)
    
#     request_data = json.loads(json_method_request.json_data)
#     print(request_data, flush=True)
    
#     with DaprClient() as client:
#         state_value = client.get_state("statestore", '+916395798956:haveFiles')
#         print("state value", state_value)
    
#     # Create a response using protobuf
#     response_data = {
#         "received": request_data,
#         "message": "JSON data received and processed"
#     }
#     response = service_pb2.JsonMethodResponse(
#         received=json.dumps(response_data),
#         message="JSON data received and processed"
#     )
#     return InvokeMethodResponse(response.SerializeToString(), "application/protobuf")

# app.run(50051)



import grpc
from concurrent import futures
import grpc_types.service_pb2 as service_pb2
import grpc_types.service_pb2_grpc as service_pb2_grpc
import json
from dapr.clients import DaprClient

class ReceiverService(service_pb2_grpc.ReceiverServiceServicer):
    def MyMethod(self, request, context):
        print(request.metadata, flush=True)
        print(request.text, flush=True)

        # Create a response using protobuf
        response = service_pb2.MyMethodResponse(message='INVOKE_RECEIVED')
        return response

    def JsonMethod(self, request, context):
        request_data = json.loads(request.json_data)
        print(request_data, flush=True)

        with DaprClient() as client:
            state_value = client.get_state("statestore", '+916395798956:haveFiles')
            print("state value", state_value)

        # Create a response using protobuf
        response_data = {
            "received": request_data,
            "message": "JSON data received and processed"
        }
        response = service_pb2.JsonMethodResponse(
            received=json.dumps(response_data),
            message="JSON data received and processed"
        )
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ReceiverServiceServicer_to_server(ReceiverService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()