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

# Example

```bash
command="-o large -t json" docker compose up --build --remove-orphans
```

```bash
command="--help" docker compose up --build --remove-orphans

serialization-client-1  | usage: __main__.py [-h]
serialization-client-1  |                    [--test {avro,json,msgpack,pickle,proto,xml,yaml} [{avro,json,msgpack,pickle,proto,xml,yaml} ...]]
serialization-client-1  |                    [--test_object {simple,medium,big,large}]
serialization-client-1  | 
serialization-client-1  | options:
serialization-client-1  |   -h, --help            show this help message and exit
serialization-client-1  |   --test {avro,json,msgpack,pickle,proto,xml,yaml} [{avro,json,msgpack,pickle,proto,xml,yaml} ...], -t {avro,json,msgpack,pickle,proto,xml,yaml} [{avro,json,msgpack,pickle,proto,xml,yaml} ...]
serialization-client-1  |                         Choose a format for testing
serialization-client-1  |   --test_object {simple,medium,big,large}, -o {simple,medium,big,large}
serialization-client-1  |                         Choose an test_object for testing
serialization-client-1 exited with code 0
```
