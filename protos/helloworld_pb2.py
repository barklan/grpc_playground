# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='protos',
  syntax='proto3',
  serialized_options=b'Z4github.com/barklan/grpc_playground/helloworld/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\x06protos\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\x0cQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\"\x1a\n\nQueryReply\x12\x0c\n\x04rows\x18\x01 \x03(\t2v\n\x07Greeter\x12\x36\n\x08SayHello\x12\x14.protos.HelloRequest\x1a\x12.protos.HelloReply\"\x00\x12\x33\n\x05Query\x12\x14.protos.QueryRequest\x1a\x12.protos.QueryReply\"\x00\x42\x36Z4github.com/barklan/grpc_playground/helloworld/protosb\x06proto3'
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='protos.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protos.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=56,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='protos.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='protos.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=87,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='protos.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='protos.QueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=118,
)


_QUERYREPLY = _descriptor.Descriptor(
  name='QueryReply',
  full_name='protos.QueryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='protos.QueryReply.rows', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryReply'] = _QUERYREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:protos.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:protos.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:protos.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryReply = _reflection.GeneratedProtocolMessageType('QueryReply', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:protos.QueryReply)
  })
_sym_db.RegisterMessage(QueryReply)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='protos.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=148,
  serialized_end=266,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='protos.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='protos.Greeter.Query',
    index=1,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)