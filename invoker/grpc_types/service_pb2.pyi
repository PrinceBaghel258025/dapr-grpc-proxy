from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MyMethodRequest(_message.Message):
    __slots__ = ("metadata", "text")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    text: str
    def __init__(self, metadata: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class MyMethodResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class JsonMethodRequest(_message.Message):
    __slots__ = ("json_data",)
    JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    json_data: str
    def __init__(self, json_data: _Optional[str] = ...) -> None: ...

class JsonMethodResponse(_message.Message):
    __slots__ = ("received", "message")
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    received: str
    message: str
    def __init__(self, received: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
