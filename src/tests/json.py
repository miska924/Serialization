import json
import logging
import os

from src.tests.base_test import BaseTest


class JsonTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, object):
        return json.dumps(object)

    def deserialize(self, serialised):
        return json.loads(serialised)
