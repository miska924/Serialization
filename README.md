# Serialization

```bash
docker build . -t app:1.0 && docker run app:1.0
```
```bash
usage: __main__.py [-h] [--test {avro,json,msgpack,pickle,proto,xml,yaml} [{avro,json,msgpack,pickle,proto,xml,yaml} ...]] [--object {simple,medium,big,large}]
                   [--verbose]

options:
  -h, --help            show this help message and exit
  --test {avro,json,msgpack,pickle,proto,xml,yaml} [{avro,json,msgpack,pickle,proto,xml,yaml} ...], -t {avro,json,msgpack,pickle,proto,xml,yaml} [{avro,json,msgpack,pickle,proto,xml,yaml} ...]
                        Choose a format for testing
  --object {simple,medium,big,large}, -o {simple,medium,big,large}
                        Choose an object for testing
  --verbose, -v
```