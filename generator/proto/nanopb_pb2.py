# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nanopb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nanopb.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\030fi.kapsi.koti.jpa.nanopb'),
  serialized_pb=_b('\n\x0cnanopb.proto\x1a google/protobuf/descriptor.proto\"\xf4\x05\n\rNanoPBOptions\x12\x10\n\x08max_size\x18\x01 \x01(\x05\x12\x12\n\nmax_length\x18\x0e \x01(\x05\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12&\n\x08int_size\x18\x07 \x01(\x0e\x32\x08.IntSize:\nIS_DEFAULT\x12$\n\x04type\x18\x03 \x01(\x0e\x32\n.FieldType:\nFT_DEFAULT\x12\x18\n\nlong_names\x18\x04 \x01(\x08:\x04true\x12\x1c\n\rpacked_struct\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0bpacked_enum\x18\n \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cskip_message\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x18\n\tno_unions\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\r\n\x05msgid\x18\t \x01(\r\x12\x1e\n\x0f\x61nonymous_oneof\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06proto3\x18\x0c \x01(\x08:\x05\x66\x61lse\x12#\n\x14proto3_singular_msgs\x18\x15 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0e\x65num_to_string\x18\r \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0c\x66ixed_length\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0b\x66ixed_count\x18\x10 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fsubmsg_callback\x18\x16 \x01(\x08:\x05\x66\x61lse\x12/\n\x0cmangle_names\x18\x11 \x01(\x0e\x32\x11.TypenameMangling:\x06M_NONE\x12(\n\x11\x63\x61llback_datatype\x18\x12 \x01(\t:\rpb_callback_t\x12\x34\n\x11\x63\x61llback_function\x18\x13 \x01(\t:\x19pb_default_field_callback\x12\x30\n\x0e\x64\x65scriptorsize\x18\x14 \x01(\x0e\x32\x0f.DescriptorSize:\x07\x44S_AUTO\x12\x1a\n\x0b\x64\x65\x66\x61ult_has\x18\x17 \x01(\x08:\x05\x66\x61lse\x12\x0f\n\x07include\x18\x18 \x03(\t*i\n\tFieldType\x12\x0e\n\nFT_DEFAULT\x10\x00\x12\x0f\n\x0b\x46T_CALLBACK\x10\x01\x12\x0e\n\nFT_POINTER\x10\x04\x12\r\n\tFT_STATIC\x10\x02\x12\r\n\tFT_IGNORE\x10\x03\x12\r\n\tFT_INLINE\x10\x05*D\n\x07IntSize\x12\x0e\n\nIS_DEFAULT\x10\x00\x12\x08\n\x04IS_8\x10\x08\x12\t\n\x05IS_16\x10\x10\x12\t\n\x05IS_32\x10 \x12\t\n\x05IS_64\x10@*Z\n\x10TypenameMangling\x12\n\n\x06M_NONE\x10\x00\x12\x13\n\x0fM_STRIP_PACKAGE\x10\x01\x12\r\n\tM_FLATTEN\x10\x02\x12\x16\n\x12M_PACKAGE_INITIALS\x10\x03*E\n\x0e\x44\x65scriptorSize\x12\x0b\n\x07\x44S_AUTO\x10\x00\x12\x08\n\x04\x44S_1\x10\x01\x12\x08\n\x04\x44S_2\x10\x02\x12\x08\n\x04\x44S_4\x10\x04\x12\x08\n\x04\x44S_8\x10\x08:E\n\x0enanopb_fileopt\x12\x1c.google.protobuf.FileOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions:G\n\rnanopb_msgopt\x12\x1f.google.protobuf.MessageOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions:E\n\x0enanopb_enumopt\x12\x1c.google.protobuf.EnumOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions:>\n\x06nanopb\x12\x1d.google.protobuf.FieldOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptionsB\x1a\n\x18\x66i.kapsi.koti.jpa.nanopb')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FT_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_CALLBACK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_POINTER', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_STATIC', index=3, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_IGNORE', index=4, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_INLINE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=809,
  serialized_end=914,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE)

FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
_INTSIZE = _descriptor.EnumDescriptor(
  name='IntSize',
  full_name='IntSize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IS_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_8', index=1, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_16', index=2, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_32', index=3, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_64', index=4, number=64,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=916,
  serialized_end=984,
)
_sym_db.RegisterEnumDescriptor(_INTSIZE)

IntSize = enum_type_wrapper.EnumTypeWrapper(_INTSIZE)
_TYPENAMEMANGLING = _descriptor.EnumDescriptor(
  name='TypenameMangling',
  full_name='TypenameMangling',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='M_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M_STRIP_PACKAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M_FLATTEN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='M_PACKAGE_INITIALS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=986,
  serialized_end=1076,
)
_sym_db.RegisterEnumDescriptor(_TYPENAMEMANGLING)

TypenameMangling = enum_type_wrapper.EnumTypeWrapper(_TYPENAMEMANGLING)
_DESCRIPTORSIZE = _descriptor.EnumDescriptor(
  name='DescriptorSize',
  full_name='DescriptorSize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DS_AUTO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS_2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS_4', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS_8', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1078,
  serialized_end=1147,
)
_sym_db.RegisterEnumDescriptor(_DESCRIPTORSIZE)

DescriptorSize = enum_type_wrapper.EnumTypeWrapper(_DESCRIPTORSIZE)
FT_DEFAULT = 0
FT_CALLBACK = 1
FT_POINTER = 4
FT_STATIC = 2
FT_IGNORE = 3
FT_INLINE = 5
IS_DEFAULT = 0
IS_8 = 8
IS_16 = 16
IS_32 = 32
IS_64 = 64
M_NONE = 0
M_STRIP_PACKAGE = 1
M_FLATTEN = 2
M_PACKAGE_INITIALS = 3
DS_AUTO = 0
DS_1 = 1
DS_2 = 2
DS_4 = 4
DS_8 = 8

NANOPB_FILEOPT_FIELD_NUMBER = 1010
nanopb_fileopt = _descriptor.FieldDescriptor(
  name='nanopb_fileopt', full_name='nanopb_fileopt', index=0,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
NANOPB_MSGOPT_FIELD_NUMBER = 1010
nanopb_msgopt = _descriptor.FieldDescriptor(
  name='nanopb_msgopt', full_name='nanopb_msgopt', index=1,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
NANOPB_ENUMOPT_FIELD_NUMBER = 1010
nanopb_enumopt = _descriptor.FieldDescriptor(
  name='nanopb_enumopt', full_name='nanopb_enumopt', index=2,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
NANOPB_FIELD_NUMBER = 1010
nanopb = _descriptor.FieldDescriptor(
  name='nanopb', full_name='nanopb', index=3,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_NANOPBOPTIONS = _descriptor.Descriptor(
  name='NanoPBOptions',
  full_name='NanoPBOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_size', full_name='NanoPBOptions.max_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_length', full_name='NanoPBOptions.max_length', index=1,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_count', full_name='NanoPBOptions.max_count', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_size', full_name='NanoPBOptions.int_size', index=3,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='NanoPBOptions.type', index=4,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_names', full_name='NanoPBOptions.long_names', index=5,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packed_struct', full_name='NanoPBOptions.packed_struct', index=6,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packed_enum', full_name='NanoPBOptions.packed_enum', index=7,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip_message', full_name='NanoPBOptions.skip_message', index=8,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_unions', full_name='NanoPBOptions.no_unions', index=9,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgid', full_name='NanoPBOptions.msgid', index=10,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='anonymous_oneof', full_name='NanoPBOptions.anonymous_oneof', index=11,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto3', full_name='NanoPBOptions.proto3', index=12,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto3_singular_msgs', full_name='NanoPBOptions.proto3_singular_msgs', index=13,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_to_string', full_name='NanoPBOptions.enum_to_string', index=14,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_length', full_name='NanoPBOptions.fixed_length', index=15,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_count', full_name='NanoPBOptions.fixed_count', index=16,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submsg_callback', full_name='NanoPBOptions.submsg_callback', index=17,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mangle_names', full_name='NanoPBOptions.mangle_names', index=18,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback_datatype', full_name='NanoPBOptions.callback_datatype', index=19,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("pb_callback_t").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback_function', full_name='NanoPBOptions.callback_function', index=20,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("pb_default_field_callback").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptorsize', full_name='NanoPBOptions.descriptorsize', index=21,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_has', full_name='NanoPBOptions.default_has', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include', full_name='NanoPBOptions.include', index=23,
      number=24, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=807,
)

_NANOPBOPTIONS.fields_by_name['int_size'].enum_type = _INTSIZE
_NANOPBOPTIONS.fields_by_name['type'].enum_type = _FIELDTYPE
_NANOPBOPTIONS.fields_by_name['mangle_names'].enum_type = _TYPENAMEMANGLING
_NANOPBOPTIONS.fields_by_name['descriptorsize'].enum_type = _DESCRIPTORSIZE
DESCRIPTOR.message_types_by_name['NanoPBOptions'] = _NANOPBOPTIONS
DESCRIPTOR.enum_types_by_name['FieldType'] = _FIELDTYPE
DESCRIPTOR.enum_types_by_name['IntSize'] = _INTSIZE
DESCRIPTOR.enum_types_by_name['TypenameMangling'] = _TYPENAMEMANGLING
DESCRIPTOR.enum_types_by_name['DescriptorSize'] = _DESCRIPTORSIZE
DESCRIPTOR.extensions_by_name['nanopb_fileopt'] = nanopb_fileopt
DESCRIPTOR.extensions_by_name['nanopb_msgopt'] = nanopb_msgopt
DESCRIPTOR.extensions_by_name['nanopb_enumopt'] = nanopb_enumopt
DESCRIPTOR.extensions_by_name['nanopb'] = nanopb
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NanoPBOptions = _reflection.GeneratedProtocolMessageType('NanoPBOptions', (_message.Message,), {
  'DESCRIPTOR' : _NANOPBOPTIONS,
  '__module__' : 'nanopb_pb2'
  # @@protoc_insertion_point(class_scope:NanoPBOptions)
  })
_sym_db.RegisterMessage(NanoPBOptions)

nanopb_fileopt.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(nanopb_fileopt)
nanopb_msgopt.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(nanopb_msgopt)
nanopb_enumopt.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(nanopb_enumopt)
nanopb.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nanopb)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
