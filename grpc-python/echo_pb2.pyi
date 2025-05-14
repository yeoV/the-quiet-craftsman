from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class echoRequest(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class echoResponse(_message.Message):
    __slots__ = ("echo_text",)
    ECHO_TEXT_FIELD_NUMBER: _ClassVar[int]
    echo_text: str
    def __init__(self, echo_text: _Optional[str] = ...) -> None: ...
