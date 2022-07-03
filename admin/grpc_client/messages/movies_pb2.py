# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movies.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmovies.proto\x12\x06movies\"\x15\n\x05Genre\x12\x0c\n\x04name\x18\x01 \x01(\t\")\n\x06Person\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"x\n\x05Movie\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06rating\x18\x04 \x01(\t\x12\x0e\n\x06genres\x18\x05 \x03(\t\x12\x1f\n\x07persons\x18\x06 \x03(\x0b\x32\x0e.movies.Person\"1\n\x10GetMoviesRequest\x12\x1d\n\x06movies\x18\x01 \x03(\x0b\x32\r.movies.Movie\"0\n\x0fGetMoviesResult\x12\x1d\n\x06movies\x18\x01 \x01(\x0b\x32\r.movies.Movie2J\n\x06Movies\x12@\n\tGetMovies\x12\x18.movies.GetMoviesRequest\x1a\x17.movies.GetMoviesResult\"\x00\x62\x06proto3')



_GENRE = DESCRIPTOR.message_types_by_name['Genre']
_PERSON = DESCRIPTOR.message_types_by_name['Person']
_MOVIE = DESCRIPTOR.message_types_by_name['Movie']
_GETMOVIESREQUEST = DESCRIPTOR.message_types_by_name['GetMoviesRequest']
_GETMOVIESRESULT = DESCRIPTOR.message_types_by_name['GetMoviesResult']
Genre = _reflection.GeneratedProtocolMessageType('Genre', (_message.Message,), {
  'DESCRIPTOR' : _GENRE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:movies.Genre)
  })
_sym_db.RegisterMessage(Genre)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:movies.Person)
  })
_sym_db.RegisterMessage(Person)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), {
  'DESCRIPTOR' : _MOVIE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:movies.Movie)
  })
_sym_db.RegisterMessage(Movie)

GetMoviesRequest = _reflection.GeneratedProtocolMessageType('GetMoviesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMOVIESREQUEST,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:movies.GetMoviesRequest)
  })
_sym_db.RegisterMessage(GetMoviesRequest)

GetMoviesResult = _reflection.GeneratedProtocolMessageType('GetMoviesResult', (_message.Message,), {
  'DESCRIPTOR' : _GETMOVIESRESULT,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:movies.GetMoviesResult)
  })
_sym_db.RegisterMessage(GetMoviesResult)

_MOVIES = DESCRIPTOR.services_by_name['Movies']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=24
  _GENRE._serialized_end=45
  _PERSON._serialized_start=47
  _PERSON._serialized_end=88
  _MOVIE._serialized_start=90
  _MOVIE._serialized_end=210
  _GETMOVIESREQUEST._serialized_start=212
  _GETMOVIESREQUEST._serialized_end=261
  _GETMOVIESRESULT._serialized_start=263
  _GETMOVIESRESULT._serialized_end=311
  _MOVIES._serialized_start=313
  _MOVIES._serialized_end=387
# @@protoc_insertion_point(module_scope)
