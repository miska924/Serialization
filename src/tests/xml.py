import logging
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml, LOG

from src.tests.base_test import BaseTest

LOG.disabled = True


class XmlTest(BaseTest):
    def __init__(self):
        logging.info("")

    def transform(self, object):
        return ET.fromstring(dicttoxml(object))

    def serialize(self, object):
        return ET.tostring(object)

    def deserialize(self, serialised):
        return ET.fromstring(serialised)

    def comparable(self, object):
        return ET.tostring(object)
