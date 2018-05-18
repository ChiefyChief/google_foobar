class UnitTest:

    def __init__(self, data, n, expected_result):
        self.data = data
        self.n = n
        self.expected_result = expected_result


def answer(data, n):
    """
    :param data: list of task numbers [integers] for a specific minion to work on.
    :param n: integer that represents the maximum number of tasks before minions complain.
    :return: list of task numbers for a minion to work on without hitting 'Too many tasks'
    """

    updated_tasks = []

    for task_number in data:
        if not data.count(task_number) > n:
            updated_tasks.append(task_number)

    return updated_tasks


if __name__ == "__main__":

    unit_tests = [UnitTest([1, 2, 3], 0, []),
                  UnitTest([1, 2, 2, 3, 3, 3, 4, 5, 5], 1, [1, 4]),
                  UnitTest([1, 2, 3], 6, [1, 2, 3])
                  ]

    count = 0

    for test in unit_tests:
        count += 1
        result = answer(test.data, test.n)

        if result != test.expected_result:
            print "[!] Test {} failed.".format(count)
            print "\tdata: {}".format(test.data)
            print "\tn: {}".format(test.n)
            print "\texpected result: {}".format(test.expected_result)
            print "\tactual result: {}".format(result)
        else:
            print "[+] Test {} passed.".format(count)

