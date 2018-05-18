class UnitTest:

    def __init__(self, src, dst, expected_result):
        self.src = src
        self.dst = dst
        self.expected_result = expected_result


def answer(src, dst):
    return True


if __name__ == "__main__":

    unit_tests = [UnitTest(19, 36, 1),
                  UnitTest(0, 1, 3)
                  ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.src, test.dst)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\tsrc: {}".format(test.src)
            print "\tdst: {}".format(test.dst)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

