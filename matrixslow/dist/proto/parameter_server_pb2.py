# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parameter_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='parameter_server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16parameter_server.proto\"\'\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnode_type\x18\x02 \x01(\t\"&\n\x08Gradient\x12\r\n\x05value\x18\x01 \x03(\x02\x12\x0b\n\x03\x64im\x18\x02 \x03(\x05\"S\n\rNodeGradients\x12\x14\n\x05nodes\x18\x01 \x03(\x0b\x32\x05.Node\x12\x1c\n\tgradients\x18\x02 \x03(\x0b\x32\t.Gradient\x12\x0e\n\x06\x61\x63\x63_no\x18\x03 \x01(\x05\"I\n\x10ParameterPushReq\x12\r\n\x05token\x18\x01 \x01(\x04\x12&\n\x0enode_gradients\x18\x02 \x01(\x0b\x32\x0e.NodeGradients\"\"\n\x11ParameterPushResp\x12\r\n\x05token\x18\x01 \x01(\x04\"7\n\x10ParameterPullReq\x12\r\n\x05token\x18\x01 \x01(\x04\x12\x14\n\x05nodes\x18\x02 \x03(\x0b\x32\x05.Node\"J\n\x11ParameterPullResp\x12\r\n\x05token\x18\x01 \x01(\x04\x12&\n\x0enode_gradients\x18\x02 \x01(\x0b\x32\x0e.NodeGradients2t\n\x10ParameterService\x12/\n\x04Push\x12\x11.ParameterPushReq\x1a\x12.ParameterPushResp\"\x00\x12/\n\x04Pull\x12\x11.ParameterPullReq\x1a\x12.ParameterPullResp\"\x00\x62\x06proto3')
)




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_type', full_name='Node.node_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=26,
  serialized_end=65,
)


_GRADIENT = _descriptor.Descriptor(
  name='Gradient',
  full_name='Gradient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Gradient.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim', full_name='Gradient.dim', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=67,
  serialized_end=105,
)


_NODEGRADIENTS = _descriptor.Descriptor(
  name='NodeGradients',
  full_name='NodeGradients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='NodeGradients.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradients', full_name='NodeGradients.gradients', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_no', full_name='NodeGradients.acc_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=107,
  serialized_end=190,
)


_PARAMETERPUSHREQ = _descriptor.Descriptor(
  name='ParameterPushReq',
  full_name='ParameterPushReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ParameterPushReq.token', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_gradients', full_name='ParameterPushReq.node_gradients', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=192,
  serialized_end=265,
)


_PARAMETERPUSHRESP = _descriptor.Descriptor(
  name='ParameterPushResp',
  full_name='ParameterPushResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ParameterPushResp.token', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=267,
  serialized_end=301,
)


_PARAMETERPULLREQ = _descriptor.Descriptor(
  name='ParameterPullReq',
  full_name='ParameterPullReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ParameterPullReq.token', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='ParameterPullReq.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=303,
  serialized_end=358,
)


_PARAMETERPULLRESP = _descriptor.Descriptor(
  name='ParameterPullResp',
  full_name='ParameterPullResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ParameterPullResp.token', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_gradients', full_name='ParameterPullResp.node_gradients', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=360,
  serialized_end=434,
)

_NODEGRADIENTS.fields_by_name['nodes'].message_type = _NODE
_NODEGRADIENTS.fields_by_name['gradients'].message_type = _GRADIENT
_PARAMETERPUSHREQ.fields_by_name['node_gradients'].message_type = _NODEGRADIENTS
_PARAMETERPULLREQ.fields_by_name['nodes'].message_type = _NODE
_PARAMETERPULLRESP.fields_by_name['node_gradients'].message_type = _NODEGRADIENTS
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Gradient'] = _GRADIENT
DESCRIPTOR.message_types_by_name['NodeGradients'] = _NODEGRADIENTS
DESCRIPTOR.message_types_by_name['ParameterPushReq'] = _PARAMETERPUSHREQ
DESCRIPTOR.message_types_by_name['ParameterPushResp'] = _PARAMETERPUSHRESP
DESCRIPTOR.message_types_by_name['ParameterPullReq'] = _PARAMETERPULLREQ
DESCRIPTOR.message_types_by_name['ParameterPullResp'] = _PARAMETERPULLRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  })
_sym_db.RegisterMessage(Node)

Gradient = _reflection.GeneratedProtocolMessageType('Gradient', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENT,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:Gradient)
  })
_sym_db.RegisterMessage(Gradient)

NodeGradients = _reflection.GeneratedProtocolMessageType('NodeGradients', (_message.Message,), {
  'DESCRIPTOR' : _NODEGRADIENTS,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:NodeGradients)
  })
_sym_db.RegisterMessage(NodeGradients)

ParameterPushReq = _reflection.GeneratedProtocolMessageType('ParameterPushReq', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERPUSHREQ,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:ParameterPushReq)
  })
_sym_db.RegisterMessage(ParameterPushReq)

ParameterPushResp = _reflection.GeneratedProtocolMessageType('ParameterPushResp', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERPUSHRESP,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:ParameterPushResp)
  })
_sym_db.RegisterMessage(ParameterPushResp)

ParameterPullReq = _reflection.GeneratedProtocolMessageType('ParameterPullReq', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERPULLREQ,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:ParameterPullReq)
  })
_sym_db.RegisterMessage(ParameterPullReq)

ParameterPullResp = _reflection.GeneratedProtocolMessageType('ParameterPullResp', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERPULLRESP,
  '__module__' : 'parameter_server_pb2'
  # @@protoc_insertion_point(class_scope:ParameterPullResp)
  })
_sym_db.RegisterMessage(ParameterPullResp)



_PARAMETERSERVICE = _descriptor.ServiceDescriptor(
  name='ParameterService',
  full_name='ParameterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=436,
  serialized_end=552,
  methods=[
  _descriptor.MethodDescriptor(
    name='Push',
    full_name='ParameterService.Push',
    index=0,
    containing_service=None,
    input_type=_PARAMETERPUSHREQ,
    output_type=_PARAMETERPUSHRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Pull',
    full_name='ParameterService.Pull',
    index=1,
    containing_service=None,
    input_type=_PARAMETERPULLREQ,
    output_type=_PARAMETERPULLRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMETERSERVICE)

DESCRIPTOR.services_by_name['ParameterService'] = _PARAMETERSERVICE

# @@protoc_insertion_point(module_scope)