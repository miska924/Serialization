from importlib import resources
import json
from enum import Enum


class TestObject(Enum):
    SIMPLE = "simple"
    MEDIUM = "medium"
    BIG = "big"
    LARGE = "large"


files = resources.files("src.tests.objects")

OBJECTS = {
    TestObject.SIMPLE: json.loads(files.joinpath("simple.json").read_text()),
    TestObject.MEDIUM: json.loads(files.joinpath("medium.json").read_text()),
    TestObject.BIG: json.loads(files.joinpath("big.json").read_text()),
    TestObject.LARGE: json.loads(files.joinpath("large.json").read_text()),
}
