import logging
import msgpack

from src.tests.base_test import BaseTest


class MsgpackTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, test_object):
        return msgpack.packb(test_object)

    def deserialize(self, serialized):
        return msgpack.unpackb(serialized)
