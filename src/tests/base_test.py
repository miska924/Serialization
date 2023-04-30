import datetime
import json
import logging


class BaseTest:
    def __init__(self, **kwargs):
        raise NotImplementedError()

    def run(self, test_object=None):
        test_object = self.transform(test_object)

        start = datetime.datetime.now()
        serialized = self.serialize(test_object)
        deserialized = self.deserialize(serialized)
        end = datetime.datetime.now()

        logging.info("Time elapsed: %s", end - start)

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
