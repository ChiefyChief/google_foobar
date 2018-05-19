class UnitTest:

    def __init__(self, src, dst, expected_result):
        self.src = src
        self.dst = dst
        self.expected_result = expected_result


class ChessGame:

    def __init__(self, src, dst):
        self.matrix = self.build_matrix()
        self.src = src
        self.dst = dst
        self.sx, self.sy = find_point(self.matrix, self.src)
        self.dx, self.dy = find_point(self.matrix, self.dst)


    def build_matrix(self):
        matrix = []
        matrix_count = 0

        for _ in range(8):
            new_row = []
            for _ in range(8):
                new_row.append(matrix_count)
                matrix_count += 1
            matrix.append(new_row)

        return matrix


def find_point(matrix, number):
    found = False
    x = 0
    y = 0

    for row in matrix:
        x = 0
        for element in row:

            if element == number:
                found = True
                break
            else:
                x += 1

        if found:
            break
        else:
            y += 1

    return x, y


def generate_next_moves(start_x, start_y, game, depth=1, already_searched=[]):
    potential_moves = [(-2, -1), (-2, 1),
                       (-1, -2), (-1, 2),
                       (1, -2), (1, 2),
                       (2, -1), (2, 1)
                       ]

    already_searched.append((start_x, start_y))

    print "Start X: " + str(start_x)
    print "Start Y: " + str(start_y)
    for pot_x, pot_y in potential_moves:
        next_x = start_x + pot_x
        next_y = start_y + pot_y
        next = (next_x, next_y)

        if next_x in range(8) and next_y in range(8) and next not in already_searched:

            print "Next X: " + str(next_x)
            print "Next Y: " + str(next_y)
            print "Move X: " + str(pot_x)
            print "Move Y: " + str(pot_y)
            print game.matrix[next_x][next_y]
            raw_input()

            if next_x == game.dx and next_y == game.dy:
                return depth
            else:
                generate_next_moves(next_x, next_y, game, depth + 1, already_searched)



def answer(src, dst):
    game = ChessGame(src, dst)
    depth = generate_next_moves(game.sx, game.sy, game)

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

