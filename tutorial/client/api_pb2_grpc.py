# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import api_pb2 as api__pb2


class UserGuideStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPoint = channel.unary_unary(
        '/api.UserGuide/GetPoint',
        request_serializer=api__pb2.Profile.SerializeToString,
        response_deserializer=api__pb2.Point.FromString,
        )
    self.ListUsers = channel.unary_stream(
        '/api.UserGuide/ListUsers',
        request_serializer=api__pb2.Point.SerializeToString,
        response_deserializer=api__pb2.User.FromString,
        )


class UserGuideServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPoint(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserGuideServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPoint': grpc.unary_unary_rpc_method_handler(
          servicer.GetPoint,
          request_deserializer=api__pb2.Profile.FromString,
          response_serializer=api__pb2.Point.SerializeToString,
      ),
      'ListUsers': grpc.unary_stream_rpc_method_handler(
          servicer.ListUsers,
          request_deserializer=api__pb2.Point.FromString,
          response_serializer=api__pb2.User.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.UserGuide', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
