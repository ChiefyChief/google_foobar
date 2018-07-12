class UnitTest:

    def __init__(self, m, f, expected_result):
        self.m = m
        self.f = f
        self.expected_result = expected_result


def answer(m, f):
    """
    :param m: [int] number of Mach bombs needed
    :param f: [int] number of Facula bombs needed
    :return: minimum number of iterations to produce a strong enough combo
    """

    generations = 0
    current_iteration = [m, f]
    
    while min(current_iteration) > 1 and max(current_iteration) > 1:
        if divmod(int(max(current_iteration)), int(min(current_iteration)))[-1] == 0:
            return "impossible"
        
        generations += int(max(current_iteration)) // int(min(current_iteration))
        current_iteration.sort()
        current_iteration[-1]  = divmod(int(max(current_iteration)), int(min(current_iteration)))[1]

    return generations + max(current_iteration) - 1


if __name__ == "__main__":

    unit_tests = [UnitTest(2, 1, 1),
                  UnitTest(4, 7, 4),
                  UnitTest(2, 4, "impossible")
                 ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.m, test.f)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\tm: {}".format(test.m)
            print "\tf: {}".format(test.f)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

