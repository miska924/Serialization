import fastavro
import logging

from io import BytesIO

from src.tests.avro import SCHEMA
from src.tests.base_test import BaseTest


class AvroTest(BaseTest):
    def __init__(self):
        logging.info("")

    def serialize(self, object):
        bytes_writer = BytesIO()
        fastavro.schemaless_writer(bytes_writer, SCHEMA, object)
        return bytes_writer.getvalue()

    def deserialize(self, serialised):
        bytes_writer = BytesIO()
        bytes_writer.write(serialised)
        bytes_writer.seek(0)

        data = fastavro.schemaless_reader(bytes_writer, SCHEMA)
        return data
