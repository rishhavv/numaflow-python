# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tmap.proto\x12\x06map.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\x01\n\nMapRequest\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12.\n\nevent_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\twatermark\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"o\n\x0bMapResponse\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.map.v1.MapResponse.Result\x1a\x33\n\x06Result\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0c\n\x04tags\x18\x03 \x03(\t"\x1e\n\rReadyResponse\x12\r\n\x05ready\x18\x01 \x01(\x08\x32q\n\x03Map\x12\x30\n\x05MapFn\x12\x12.map.v1.MapRequest\x1a\x13.map.v1.MapResponse\x12\x38\n\x07IsReady\x12\x16.google.protobuf.Empty\x1a\x15.map.v1.ReadyResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "map_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_MAPREQUEST"]._serialized_start = 84
    _globals["_MAPREQUEST"]._serialized_end = 220
    _globals["_MAPRESPONSE"]._serialized_start = 222
    _globals["_MAPRESPONSE"]._serialized_end = 333
    _globals["_MAPRESPONSE_RESULT"]._serialized_start = 282
    _globals["_MAPRESPONSE_RESULT"]._serialized_end = 333
    _globals["_READYRESPONSE"]._serialized_start = 335
    _globals["_READYRESPONSE"]._serialized_end = 365
    _globals["_MAP"]._serialized_start = 367
    _globals["_MAP"]._serialized_end = 480
# @@protoc_insertion_point(module_scope)
