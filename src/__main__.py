from src import (
    parse_args,
    setup_logging,
    TestObject,
    TestCase,
    TEST_CASE_TO_TEST,
    OBJECTS,
)


def main():
    args = parse_args()
    setup_logging(args)

    object = OBJECTS[TestObject(args.object)]

    tests = (
        [e for e in TestCase]
        if "all" in args.test
        else [TestCase(item) for item in args.test]
    )

    for test in tests:
        TEST_CASE_TO_TEST[TestCase(test)]().run(object)


if __name__ == "__main__":
    main()
