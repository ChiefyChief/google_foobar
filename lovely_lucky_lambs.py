class UnitTest:

    def __init__(self, total_lambs, expected_result):
        self.total_lambs = total_lambs
        self.expected_result = expected_result


def get_generous(total_lambs):
    """
    :param total_lambs: [int] number of lambs to divvy out
    :return: [int] number of henchmen that I can hire by being generous.
    """

    henchmen = 1
    total_lambs -= 1

    last = 0
    current = 1

    while total_lambs > 0:
        if total_lambs < current * 2:  # This is our final loop to handle an edge case [based on the rules].
            if total_lambs >= current + last:
                return henchmen + 1
            else:
                return henchmen
        else:  # We can keep going!
            henchmen += 1
            last = current
            current *= 2
            total_lambs -= current

    return henchmen


def get_stingy(total_lambs):
    """
    :param total_lambs: [int] number of lambs to divvy out
    :return: [int] number of henchmen that I can hire by being stingy.
    """

    henchmen = 1
    total_lambs_left = 1
    current = total_lambs - total_lambs_left

    if current == 0:
        return henchmen

    last = 1
    current -= last
    henchmen += 1

    while current > 0:
        num_lambs = last + total_lambs_left
        current -= num_lambs

        if current >= 0:
            henchmen += 1
            total_lambs_left = last
            last = num_lambs

    return henchmen


def answer(total_lambs):
    """
    :param total_lambs: list of task numbers [integers] for a specific minion to work on.
    :return: list of task numbers for a minion to work on without hitting 'Too many tasks'
    """

    return get_stingy(total_lambs) - get_generous(total_lambs)


if __name__ == "__main__":

    unit_tests = [UnitTest(10, 1),
                  UnitTest(143, 3)
                  ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.total_lambs)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\ttotal_lambs: {}".format(test.total_lambs)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

