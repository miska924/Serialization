import socket
import logging
import json
import random
import time
import os

from src import (
    parse_args,
    TestObject,
    TestCase,
    TEST_CASE_TO_TEST,
    OBJECTS,
)


if __name__ == "__main__":
    time.sleep(2)
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
    )

    logging.debug(args)

    client_address = ("client", 2925)
    server_addresses = [
        ("server-msgpack", 2919),
        ("server-yaml", 2920),
        ("server-avro", 2921),
        ("server-proto", 2922),
        ("server-json", 2923),
        ("server-xml", 2924),
    ]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(client_address)
    logging.debug("binded")

    request = " ".join(["/get_result", str(args.test_object), " ".join(args.test)])
    responses = []
    for server_address in server_addresses:
        client_socket.sendto(request.encode("utf-8"), server_address)
        response, server_address = client_socket.recvfrom(1024)
        decoded = response.decode("utf-8")
        if decoded:
            logging.info(decoded)

    client_socket.close()
