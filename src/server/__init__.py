import logging
import socket
import threading

from src import (
    parse_args,
    TestObject,
    TestCase,
    TEST_CASE_TO_TEST,
    OBJECTS,
)


def perform_calculations(test_object, test_case):
    test = TEST_CASE_TO_TEST[test_case]()
    test.run(OBJECTS[TestObject(test_object)])
    return str(test.report)


def handle_client_request(args, server_socket, client_address, data):
    try:
        logging.debug(f"Установлено соединение с клиентом {client_address}")
        command = data.split()
        logging.debug(command)

        assert "/get_result" == command[0]
        assert command[1] in [obj.value for obj in TestObject]
        for c in command[2:]:
            if c == "all":
                continue
            assert c in [case.value for case in TestCase]

        tests = (
            [item for item in TestCase]
            if "all" in command[2:]
            else [TestCase(item) for item in command[2:]]
        )

        if TestCase(args.format) not in tests:
            server_socket.sendto("".encode("utf-8"), client_address)
            return
        tests = [TestCase(args.format)]
        logging.info(args.format)

        logging.debug(tests)
        result = []
        for test in tests:
            res = perform_calculations(command[1], test)
            result.append(res)
            logging.debug(res)

        server_socket.sendto("\n".join(result).encode("utf-8"), client_address)

    except Exception as e:
        server_socket.sendto(str(e).encode("utf-8"), client_address)


def start_server(args):
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
    )
    mapping = {
        "server-msgpack": 2919,
        "server-yaml": 2920,
        "server-avro": 2921,
        "server-proto": 2922,
        "server-json": 2923,
        "server-xml": 2924,
    }
    host = f"server-{args.format}"
    server_address = (host, mapping[host])
    logging.debug(server_address)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)
    logging.debug(f"Сервер запущен на {server_address[0]}:{server_address[1]}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        data = data.decode()
        logging.debug(client_address)
        handle_client_request(args, server_socket, client_address, data)
    server_socket.close()
