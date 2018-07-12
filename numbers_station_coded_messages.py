class UnitTest:

    def __init__(self, l, t, expected_result):
        self.l = l
        self.t = t
        self.expected_result = expected_result


def answer(l, t):
    """
    :param l: list of integers between 0 and 100.
    :param t: integer derived from a subset of integers from l
    :return: list of indexes [start and end] from l that sum up to equal t
    """
    for i in enumerate(l):
        for j in enumerate(l):
            if sum(l[i[0]:j[0] + 1]) == t:
                return [i[0], j[0]]
    
    return [-1, -1]


if __name__ == "__main__":

    unit_tests = [UnitTest([4, 3, 5, 7, 8], 12, [0, 2]),
                  UnitTest([4, 3, 10, 2, 8], 12, [2, 3]),
                  UnitTest([1, 2, 3, 4], 15, [-1, -1])
                  ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.l, test.t)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\tl: {}".format(test.l)
            print "\tt: {}".format(test.t)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

