# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x08receiver\"1\n\x0fMyMethodRequest\x12\x10\n\x08metadata\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"#\n\x10MyMethodResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"&\n\x11JsonMethodRequest\x12\x11\n\tjson_data\x18\x01 \x01(\t\"7\n\x12JsonMethodResponse\x12\x10\n\x08received\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\x9d\x01\n\x0fReceiverService\x12\x41\n\x08MyMethod\x12\x19.receiver.MyMethodRequest\x1a\x1a.receiver.MyMethodResponse\x12G\n\nJsonMethod\x12\x1b.receiver.JsonMethodRequest\x1a\x1c.receiver.JsonMethodResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MYMETHODREQUEST']._serialized_start=27
  _globals['_MYMETHODREQUEST']._serialized_end=76
  _globals['_MYMETHODRESPONSE']._serialized_start=78
  _globals['_MYMETHODRESPONSE']._serialized_end=113
  _globals['_JSONMETHODREQUEST']._serialized_start=115
  _globals['_JSONMETHODREQUEST']._serialized_end=153
  _globals['_JSONMETHODRESPONSE']._serialized_start=155
  _globals['_JSONMETHODRESPONSE']._serialized_end=210
  _globals['_RECEIVERSERVICE']._serialized_start=213
  _globals['_RECEIVERSERVICE']._serialized_end=370
# @@protoc_insertion_point(module_scope)