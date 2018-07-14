class UnitTest:

    def __init__(self, n, expected_result):
        self.n = n
        self.expected_result = expected_result


def answer(n):
    """
    :param m: [int] number of pellets
    :return: number of transformations needed to get to 1 pellet
    """

    return True


if __name__ == "__main__":

    unit_tests = [UnitTest(4, 2),
                  UnitTest(15, 5)
                 ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.n)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\tn: {}".format(test.n)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

