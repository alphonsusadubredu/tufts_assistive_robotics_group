# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from encoder_msgs/Encoder.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Encoder(genpy.Message):
  _md5sum = "b66af2928dcdc45aac405392cc8c0f5c"
  _type = "encoder_msgs/Encoder"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 time_stamp
int64 left_encoder_count
int64 right_encoder_count
"""
  __slots__ = ['time_stamp','left_encoder_count','right_encoder_count']
  _slot_types = ['float32','int64','int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_stamp,left_encoder_count,right_encoder_count

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Encoder, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_stamp is None:
        self.time_stamp = 0.
      if self.left_encoder_count is None:
        self.left_encoder_count = 0
      if self.right_encoder_count is None:
        self.right_encoder_count = 0
    else:
      self.time_stamp = 0.
      self.left_encoder_count = 0
      self.right_encoder_count = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_f2q().pack(_x.time_stamp, _x.left_encoder_count, _x.right_encoder_count))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.time_stamp, _x.left_encoder_count, _x.right_encoder_count,) = _get_struct_f2q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_f2q().pack(_x.time_stamp, _x.left_encoder_count, _x.right_encoder_count))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.time_stamp, _x.left_encoder_count, _x.right_encoder_count,) = _get_struct_f2q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_f2q = None
def _get_struct_f2q():
    global _struct_f2q
    if _struct_f2q is None:
        _struct_f2q = struct.Struct("<f2q")
    return _struct_f2q
