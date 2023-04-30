import logging
from io import BytesIO

import fastavro

from src.tests.avro import SCHEMA
from src.tests.base_test import BaseTest


class AvroTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, test_object):
        bytes_writer = BytesIO()
        fastavro.schemaless_writer(bytes_writer, SCHEMA, test_object)
        return bytes_writer.getvalue()

    def deserialize(self, serialized):
        bytes_writer = BytesIO()
        bytes_writer.write(serialized)
        bytes_writer.seek(0)

        data = fastavro.schemaless_reader(bytes_writer, SCHEMA)
        return data
