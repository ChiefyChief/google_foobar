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
    result = 0
    
    for line in range(length):
        line_start = start + line * length
        line_skip = line_start + length - line - 1
        
        if line_start != 0:
            line_start -= 1

        result ^= [line_start, 1, line_start + 1, 0][line_start % 4] ^ \
                  [line_skip, 1, line_skip + 1, 0][line_skip % 4]
        
    return result


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

