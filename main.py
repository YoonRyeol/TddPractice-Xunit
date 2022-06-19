from WasRun import WasRun


def main():
    test = WasRun("testMethod")
    print(test.wasRun)
    test.testMethod()
    print(test.wasRun)


if __name__ == "__main__":
    main()
