import logging
import pickle

from src.tests.base_test import BaseTest


class PickleTest(BaseTest):
    def serialize(self, test_object):
        return pickle.dumps(test_object)

    def deserialize(self, serialized):
        return pickle.loads(serialized)

    def format_name(self):
        return "PICKLE"
