import logging
import pickle

from src.tests.base_test import BaseTest


class PickleTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, object):
        return pickle.dumps(object)

    def deserialize(self, serialised):
        return pickle.loads(serialised)
