import logging
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml, LOG

from src.tests.base_test import BaseTest

LOG.disabled = True


class XmlTest(BaseTest):
    def __init__(self):
        logging.info("")

    def transform(self, test_object):
        return ET.fromstring(dicttoxml(test_object))

    def serialize(self, test_object):
        return ET.tostring(test_object)

    def deserialize(self, serialized):
        return ET.fromstring(serialized)

    def comparable(self, test_object):
        return ET.tostring(test_object)
