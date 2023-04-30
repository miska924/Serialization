import logging
from google.protobuf.json_format import ParseDict, MessageToJson

from src.tests.base_test import BaseTest
from src.tests.proto.some_message_pb2 import SomeMessage


class ProtoTest(BaseTest):
    def __init__(self):
        logging.info("")

    def transform(self, test_object):
        result = SomeMessage()
        return ParseDict(test_object, result)

    def serialize(self, test_object: SomeMessage):
        return test_object.SerializeToString()

    def deserialize(self, serialized: bytes):
        result = SomeMessage()
        result.ParseFromString(serialized)
        return result

    def comparable(self, test_object: SomeMessage):
        result = MessageToJson(test_object, sort_keys=True)
        return result
