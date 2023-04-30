import datetime
import json
import logging


class BaseTest:
    def __init__(self, **kwargs):
        raise NotImplementedError()

    def run(self, object=None):
        object = self.transform(object)

        start = datetime.datetime.now()
        serialized = self.serialize(object)
        deserialized = self.deserialize(serialized)
        end = datetime.datetime.now()

        logging.info(f"Time elapsed: {end - start}")

        expected = self.comparable(object)
        got = self.comparable(deserialized)

        assert expected == got

    def transform(self, object):
        return object

    def serialize(self, object):
        return object

    def deserialize(self, serialised):
        return serialised

    def comparable(self, object):
        return json.dumps(object, sort_keys=True)
