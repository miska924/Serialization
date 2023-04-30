import yaml
import logging

from src.tests.base_test import BaseTest


class YamlTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, object):
        return yaml.dump(object)

    def deserialize(self, serialised):
        return yaml.full_load(serialised)
