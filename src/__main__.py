import logging

from src import (
    parse_args,
    TestObject,
    TestCase,
    TEST_CASE_TO_TEST,
    OBJECTS,
)


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s\t%(levelname)s\t%(filename)s\t%(message)s",
    )

    test_object = OBJECTS[TestObject(args.test_object)]

    tests = (
        list(TestCase) if "all" in args.test else [TestCase(item) for item in args.test]
    )

    for test in tests:
        TEST_CASE_TO_TEST[TestCase(test)]().run(test_object)


if __name__ == "__main__":
    main()
