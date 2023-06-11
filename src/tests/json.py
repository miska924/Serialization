import json
import logging

from src.tests.base_test import BaseTest


class JsonTest(BaseTest):
    def serialize(self, test_object):
        return json.dumps(test_object)

    def deserialize(self, serialized):
        return json.loads(serialized)

    def format_name(self):
        return "JSON"
