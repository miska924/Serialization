import json
import logging

from src.tests.base_test import BaseTest


class JsonTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, test_object):
        return json.dumps(test_object)

    def deserialize(self, serialized):
        return json.loads(serialized)
