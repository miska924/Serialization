import datetime
import json
import logging
import sys


class BaseTest:
    def __init__(self, **kwargs):
        pass

    def run(self, test_object=None):
        test_object = self.transform(test_object)

        start = datetime.datetime.now()
        serialized = self.serialize(test_object)
        middle = datetime.datetime.now()
        deserialized = self.deserialize(serialized)
        end = datetime.datetime.now()

        seriaalization_time = (middle - start).microseconds // 1000
        deserialization_time = (end - middle).microseconds // 1000
        logging.info(
            f"{self.format_name()} – {str(sys.getsizeof(serialized))} – {seriaalization_time}ms – {deserialization_time}ms"
        )

        expected = self.comparable(test_object)
        got = self.comparable(deserialized)

        assert expected == got

    def transform(self, test_object):
        return test_object

    def serialize(self, test_object):
        return test_object

    def deserialize(self, serialized):
        return serialized

    def comparable(self, test_object):
        return json.dumps(test_object, sort_keys=True)

    def format_name(self):
        raise NotImplementedError()
