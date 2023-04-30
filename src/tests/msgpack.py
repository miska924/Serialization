import logging
import msgpack

from src.tests.base_test import BaseTest


class MsgpackTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, object):
        return msgpack.packb(object)

    def deserialize(self, serialised):
        return msgpack.unpackb(serialised)
