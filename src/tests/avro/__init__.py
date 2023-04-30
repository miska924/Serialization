import json
from importlib import resources


files = resources.files("src.tests.avro")

SCHEMA = json.loads(files.joinpath("schema.avro").read_text())
