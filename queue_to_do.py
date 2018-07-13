class UnitTest:

    def __init__(self, start, length, expected_result):
        self.start = start
        self.length = length
        self.expected_result = expected_result


def answer(start, length):
    """
    :param start: starting number for the line
    :param length: number of people to go through
    :return: returns the XOR of the queue(s)
    """
    return True


if __name__ == "__main__":

    unit_tests = [UnitTest(0, 3, 2),
                  UnitTest(17, 4, 14)
                  ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.start, test.length)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\tstart: {}".format(test.start)
            print "\tlength: {}".format(test.length)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

