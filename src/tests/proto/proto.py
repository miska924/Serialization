import logging
from google.protobuf.json_format import ParseDict, MessageToJson

from src.tests.base_test import BaseTest
from src.tests.proto.some_message_pb2 import SomeMessage


class ProtoTest(BaseTest):
    def __init__(self):
        logging.info("")

    def transform(self, object):
        result = SomeMessage()
        return ParseDict(object, result)

    def serialize(self, object: SomeMessage):
        return object.SerializeToString()

    def deserialize(self, object: bytes):
        result = SomeMessage()
        result.ParseFromString(object)
        return result

    def comparable(self, object: SomeMessage):
        result = MessageToJson(object, sort_keys=True)
        return result
