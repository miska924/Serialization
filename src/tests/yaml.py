import logging

import yaml

from src.tests.base_test import BaseTest


class YamlTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, test_object):
        return yaml.dump(test_object)

    def deserialize(self, serialized):
        return yaml.full_load(serialized)
