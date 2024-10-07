# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import grpc_types.service_pb2 as service__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ReceiverServiceStub(object):
    """Define the service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MyMethod = channel.unary_unary(
                '/receiver.ReceiverService/MyMethod',
                request_serializer=service__pb2.MyMethodRequest.SerializeToString,
                response_deserializer=service__pb2.MyMethodResponse.FromString,
                _registered_method=True)
        self.JsonMethod = channel.unary_unary(
                '/receiver.ReceiverService/JsonMethod',
                request_serializer=service__pb2.JsonMethodRequest.SerializeToString,
                response_deserializer=service__pb2.JsonMethodResponse.FromString,
                _registered_method=True)


class ReceiverServiceServicer(object):
    """Define the service
    """

    def MyMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JsonMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReceiverServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MyMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.MyMethod,
                    request_deserializer=service__pb2.MyMethodRequest.FromString,
                    response_serializer=service__pb2.MyMethodResponse.SerializeToString,
            ),
            'JsonMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.JsonMethod,
                    request_deserializer=service__pb2.JsonMethodRequest.FromString,
                    response_serializer=service__pb2.JsonMethodResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'receiver.ReceiverService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('receiver.ReceiverService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ReceiverService(object):
    """Define the service
    """

    @staticmethod
    def MyMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/receiver.ReceiverService/MyMethod',
            service__pb2.MyMethodRequest.SerializeToString,
            service__pb2.MyMethodResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def JsonMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/receiver.ReceiverService/JsonMethod',
            service__pb2.JsonMethodRequest.SerializeToString,
            service__pb2.JsonMethodResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
