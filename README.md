# Serialization
This tool tests different serialization/deserialition formats

It uses data with the following structure

<details>
<summary>json schema</summary>

```json
{
    "type": "object",
    "properties": {
        "list": {
        "type": "array",
        "items": [
            {
            "type": "object",
            "properties": {
                "_id": {
                "type": "string"
                },
                "index": {
                "type": "integer"
                },
                "guid": {
                "type": "string"
                },
                "isActive": {
                "type": "boolean"
                },
                "balance": {
                "type": "string"
                },
                "picture": {
                "type": "string"
                },
                "age": {
                "type": "integer"
                },
                "eyeColor": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "gender": {
                "type": "string"
                },
                "company": {
                "type": "string"
                },
                "email": {
                "type": "string"
                },
                "phone": {
                "type": "string"
                },
                "address": {
                "type": "string"
                },
                "about": {
                "type": "string"
                },
                "registered": {
                "type": "string"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "tags": {
                "type": "array",
                "items": [
                    {
                    "type": "string"
                    },
                    {
                    "type": "string"
                    },
                    {
                    "type": "string"
                    },
                    {
                    "type": "string"
                    },
                    {
                    "type": "string"
                    },
                    {
                    "type": "string"
                    },
                    {
                    "type": "string"
                    }
                ]
                },
                "friends": {
                "type": "array",
                "items": [
                    {
                    "type": "object",
                    "properties": {
                        "id": {
                        "type": "integer"
                        },
                        "name": {
                        "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "name"
                    ]
                    },
                    {
                    "type": "object",
                    "properties": {
                        "id": {
                        "type": "integer"
                        },
                        "name": {
                        "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "name"
                    ]
                    },
                    {
                    "type": "object",
                    "properties": {
                        "id": {
                        "type": "integer"
                        },
                        "name": {
                        "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "name"
                    ]
                    }
                ]
                },
                "greeting": {
                "type": "string"
                },
                "favoriteFruit": {
                "type": "string"
                }
            },
            "required": [
                "_id",
                "index",
                "guid",
                "isActive",
                "balance",
                "picture",
                "age",
                "eyeColor",
                "name",
                "gender",
                "company",
                "email",
                "phone",
                "address",
                "about",
                "registered",
                "latitude",
                "longitude",
                "tags",
                "friends",
                "greeting",
                "favoriteFruit"
            ]
            }
        ]
        }
    },
    "required": [
        "list"
    ]
}
```

</details>

<br>

# How to use

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

# With docker compose
```bash
docker compose up --build
```