# Work in progress... accidentally forgot to submit during 72 hours

class UnitTest:

    def __init__(self, src, dst, expected_result):
        self.src = src
        self.dst = dst
        self.expected_result = expected_result


def find_point(number):
    x = number / 8
    y = number % 8
    coordinate = (x, y)

    return coordinate


def generate_moves(start_x, start_y, matrix):
    # All the potential locations a knight can land during a single move.
    potential_moves = [(-2, -1), (-2, 1),
                       (-1, -2), (-1, 2),
                       (1, -2), (1, 2),
                       (2, -1), (2, 1)
                       ]

    search_moves = [(start_x, start_y)]

    while search_moves:
        current_coordinate = search_moves.pop(0)
        current_x = current_coordinate[0]
        current_y = current_coordinate[-1]

        for move_x, move_y in potential_moves:
            next_x = current_x + move_x
            next_y = current_y + move_y

            if next_x in range(0,8) and next_y in range(0,8):
                if matrix[next_x][next_y] is None:
                    matrix[next_x][next_y] = matrix[current_x][current_y] + 1
                    search_moves.append((next_x, next_y))


def answer(src, dst):
    game = ChessGame(src, dst)
    depth = generate_next_moves(game.sx, game.sy, game.matrix)

    return depth


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

