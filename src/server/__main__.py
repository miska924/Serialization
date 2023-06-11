import argparse

from src import TestCase
from src.server import start_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--format",
        "-f",
        choices=[test_case.value for test_case in TestCase],
        type=str,
        default="json",
        help="Choose a format for testing",
    )

    start_server(parser.parse_args())
