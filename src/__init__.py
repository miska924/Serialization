import argparse
import logging

from enum import Enum

from src.tests.avro.avro import AvroTest
from src.tests.json import JsonTest
from src.tests.msgpack import MsgpackTest
from src.tests.pickle import PickleTest
from src.tests.proto.proto import ProtoTest
from src.tests.xml import XmlTest
from src.tests.yaml import YamlTest

from src.tests.objects import TestObject, OBJECTS


LOGGING_FORMAT = "%(asctime)s\t%(levelname)s\t%(filename)s\t%(message)s"


class TestCase(Enum):
    AVRO = "avro"
    JSON = "json"
    MSGPACK = "msgpack"
    PICKLE = "pickle"
    PROTO = "proto"
    XML = "xml"
    YAML = "yaml"


TEST_CASE_TO_TEST = {
    TestCase.AVRO: AvroTest,
    TestCase.JSON: JsonTest,
    TestCase.MSGPACK: MsgpackTest,
    TestCase.PICKLE: PickleTest,
    TestCase.PROTO: ProtoTest,
    TestCase.XML: XmlTest,
    TestCase.YAML: YamlTest,
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        "-t",
        choices=[test_case.value for test_case in TestCase],
        type=str,
        nargs="+",
        default=["all"],
        help="Choose a format for testing",
    )
    parser.add_argument(
        "--object",
        "-o",
        choices=[test_object.value for test_object in TestObject],
        default=TestObject.LARGE.value,
        type=str,
        help="Choose an object for testing",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
    )
    args = parser.parse_args()
    return args


def setup_logging(args):
    if args.verbose == 0:
        logging.basicConfig(
            level=logging.INFO,
            format=LOGGING_FORMAT,
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format=LOGGING_FORMAT,
        )
