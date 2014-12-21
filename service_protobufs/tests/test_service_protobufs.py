import unittest

from service_protobufs import soa_pb2


class TestServiceProtobufs(unittest.TestCase):

    def test_basic_service_request(self):
        soa_pb2.ServiceRequest()
