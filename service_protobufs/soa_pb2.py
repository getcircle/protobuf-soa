# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: soa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='soa.proto',
  package='soa',
  serialized_pb=_b('\n\tsoa.proto\x12\x03soa\")\n\x07\x43ontrol\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\"}\n\tPaginator\x12\x11\n\tnext_page\x18\x01 \x01(\t\x12\x15\n\rprevious_page\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x11\n\tpage_size\x18\x04 \x01(\r\x12\x0f\n\x04page\x18\x05 \x01(\r:\x01\x31\x12\x13\n\x0btotal_pages\x18\x06 \x01(\r\"S\n\rActionControl\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12!\n\tpaginator\x18\x03 \x01(\x0b\x32\x0e.soa.Paginator\"^\n\rActionRequest\x12#\n\x07\x63ontrol\x18\x01 \x01(\x0b\x32\x12.soa.ActionControl\x12(\n\x06params\x18\x02 \x01(\x0b\x32\x18.soa.ActionRequestParams\"\x1f\n\x13\x41\x63tionRequestParams*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xba\x01\n\x14\x41\x63tionResponseResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06\x65rrors\x18\x02 \x03(\t\x12<\n\rerror_details\x18\x03 \x03(\x0b\x32%.soa.ActionResponseResult.ErrorDetail\x1a\x39\n\x0b\x45rrorDetail\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"`\n\x0e\x41\x63tionResponse\x12#\n\x07\x63ontrol\x18\x01 \x01(\x0b\x32\x12.soa.ActionControl\x12)\n\x06result\x18\x02 \x01(\x0b\x32\x19.soa.ActionResponseResult\"T\n\x0eServiceRequest\x12\x1d\n\x07\x63ontrol\x18\x01 \x01(\x0b\x32\x0c.soa.Control\x12#\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x12.soa.ActionRequest\"V\n\x0fServiceResponse\x12\x1d\n\x07\x63ontrol\x18\x01 \x01(\x0b\x32\x0c.soa.Control\x12$\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x13.soa.ActionResponse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTROL = _descriptor.Descriptor(
  name='Control',
  full_name='soa.Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='soa.Control.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service', full_name='soa.Control.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=59,
)


_PAGINATOR = _descriptor.Descriptor(
  name='Paginator',
  full_name='soa.Paginator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_page', full_name='soa.Paginator.next_page', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previous_page', full_name='soa.Paginator.previous_page', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='soa.Paginator.count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='soa.Paginator.page_size', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page', full_name='soa.Paginator.page', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_pages', full_name='soa.Paginator.total_pages', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=186,
)


_ACTIONCONTROL = _descriptor.Descriptor(
  name='ActionControl',
  full_name='soa.ActionControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='soa.ActionControl.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='soa.ActionControl.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paginator', full_name='soa.ActionControl.paginator', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=271,
)


_ACTIONREQUEST = _descriptor.Descriptor(
  name='ActionRequest',
  full_name='soa.ActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control', full_name='soa.ActionRequest.control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='soa.ActionRequest.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=367,
)


_ACTIONREQUESTPARAMS = _descriptor.Descriptor(
  name='ActionRequestParams',
  full_name='soa.ActionRequestParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=400,
)


_ACTIONRESPONSERESULT_ERRORDETAIL = _descriptor.Descriptor(
  name='ErrorDetail',
  full_name='soa.ActionResponseResult.ErrorDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='soa.ActionResponseResult.ErrorDetail.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='soa.ActionResponseResult.ErrorDetail.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detail', full_name='soa.ActionResponseResult.ErrorDetail.detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=522,
  serialized_end=579,
)

_ACTIONRESPONSERESULT = _descriptor.Descriptor(
  name='ActionResponseResult',
  full_name='soa.ActionResponseResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='soa.ActionResponseResult.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errors', full_name='soa.ActionResponseResult.errors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_details', full_name='soa.ActionResponseResult.error_details', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACTIONRESPONSERESULT_ERRORDETAIL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=589,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='soa.ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control', full_name='soa.ActionResponse.control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='soa.ActionResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=591,
  serialized_end=687,
)


_SERVICEREQUEST = _descriptor.Descriptor(
  name='ServiceRequest',
  full_name='soa.ServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control', full_name='soa.ServiceRequest.control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actions', full_name='soa.ServiceRequest.actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=773,
)


_SERVICERESPONSE = _descriptor.Descriptor(
  name='ServiceResponse',
  full_name='soa.ServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control', full_name='soa.ServiceResponse.control', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actions', full_name='soa.ServiceResponse.actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=861,
)

_ACTIONCONTROL.fields_by_name['paginator'].message_type = _PAGINATOR
_ACTIONREQUEST.fields_by_name['control'].message_type = _ACTIONCONTROL
_ACTIONREQUEST.fields_by_name['params'].message_type = _ACTIONREQUESTPARAMS
_ACTIONRESPONSERESULT_ERRORDETAIL.containing_type = _ACTIONRESPONSERESULT
_ACTIONRESPONSERESULT.fields_by_name['error_details'].message_type = _ACTIONRESPONSERESULT_ERRORDETAIL
_ACTIONRESPONSE.fields_by_name['control'].message_type = _ACTIONCONTROL
_ACTIONRESPONSE.fields_by_name['result'].message_type = _ACTIONRESPONSERESULT
_SERVICEREQUEST.fields_by_name['control'].message_type = _CONTROL
_SERVICEREQUEST.fields_by_name['actions'].message_type = _ACTIONREQUEST
_SERVICERESPONSE.fields_by_name['control'].message_type = _CONTROL
_SERVICERESPONSE.fields_by_name['actions'].message_type = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['Control'] = _CONTROL
DESCRIPTOR.message_types_by_name['Paginator'] = _PAGINATOR
DESCRIPTOR.message_types_by_name['ActionControl'] = _ACTIONCONTROL
DESCRIPTOR.message_types_by_name['ActionRequest'] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name['ActionRequestParams'] = _ACTIONREQUESTPARAMS
DESCRIPTOR.message_types_by_name['ActionResponseResult'] = _ACTIONRESPONSERESULT
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['ServiceRequest'] = _SERVICEREQUEST
DESCRIPTOR.message_types_by_name['ServiceResponse'] = _SERVICERESPONSE

Control = _reflection.GeneratedProtocolMessageType('Control', (_message.Message,), dict(
  DESCRIPTOR = _CONTROL,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.Control)
  ))
_sym_db.RegisterMessage(Control)

Paginator = _reflection.GeneratedProtocolMessageType('Paginator', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATOR,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.Paginator)
  ))
_sym_db.RegisterMessage(Paginator)

ActionControl = _reflection.GeneratedProtocolMessageType('ActionControl', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONCONTROL,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ActionControl)
  ))
_sym_db.RegisterMessage(ActionControl)

ActionRequest = _reflection.GeneratedProtocolMessageType('ActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONREQUEST,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ActionRequest)
  ))
_sym_db.RegisterMessage(ActionRequest)

ActionRequestParams = _reflection.GeneratedProtocolMessageType('ActionRequestParams', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONREQUESTPARAMS,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ActionRequestParams)
  ))
_sym_db.RegisterMessage(ActionRequestParams)

ActionResponseResult = _reflection.GeneratedProtocolMessageType('ActionResponseResult', (_message.Message,), dict(

  ErrorDetail = _reflection.GeneratedProtocolMessageType('ErrorDetail', (_message.Message,), dict(
    DESCRIPTOR = _ACTIONRESPONSERESULT_ERRORDETAIL,
    __module__ = 'soa_pb2'
    # @@protoc_insertion_point(class_scope:soa.ActionResponseResult.ErrorDetail)
    ))
  ,
  DESCRIPTOR = _ACTIONRESPONSERESULT,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ActionResponseResult)
  ))
_sym_db.RegisterMessage(ActionResponseResult)
_sym_db.RegisterMessage(ActionResponseResult.ErrorDetail)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONRESPONSE,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ActionResponse)
  ))
_sym_db.RegisterMessage(ActionResponse)

ServiceRequest = _reflection.GeneratedProtocolMessageType('ServiceRequest', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEREQUEST,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ServiceRequest)
  ))
_sym_db.RegisterMessage(ServiceRequest)

ServiceResponse = _reflection.GeneratedProtocolMessageType('ServiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVICERESPONSE,
  __module__ = 'soa_pb2'
  # @@protoc_insertion_point(class_scope:soa.ServiceResponse)
  ))
_sym_db.RegisterMessage(ServiceResponse)


# @@protoc_insertion_point(module_scope)
