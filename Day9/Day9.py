def problemOne():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    board = [[Square(True)]]
    tailIndex = [0, 0]
    headIndex = [0, 0]

    def updateIndexes():
        nonlocal board, tailIndex, headIndex
        if headIndex[0] == tailIndex[0]:
            if headIndex[1] - tailIndex[1] > 1:
                tailIndex[1] += 1
            elif tailIndex[1] - headIndex[1] > 1:
                tailIndex[1] -= 1
        elif headIndex[1] == tailIndex[1]:
            if headIndex[0] - tailIndex[0] > 1:
                tailIndex[0] += 1
            elif tailIndex[0] - headIndex[0] > 1:
                tailIndex[0] -= 1
        elif (
            abs(headIndex[0] - tailIndex[0]) != 1
            or abs(headIndex[1] - tailIndex[1]) != 1
        ):
            horizontal = 1
            vertical = 1

            if headIndex[0] < tailIndex[0]:
                vertical = -1
            if headIndex[1] < tailIndex[1]:
                horizontal = -1

            tailIndex[0] += vertical
            tailIndex[1] += horizontal

        board[tailIndex[0]][tailIndex[1]].visited = True

    for line in lines:
        [direction, numMoves] = line.split(" ")
        numMoves = int(numMoves)

        for _ in range(numMoves):
            if direction == "R":
                headIndex = [headIndex[0], headIndex[1] + 1]

                if headIndex[1] >= len(board[0]):
                    board = [b + [Square()] for b in board]
            elif direction == "L":
                headIndex = [headIndex[0], headIndex[1] - 1]

                if headIndex[1] < 0:
                    board = [[Square()] + b for b in board]
                    headIndex[1] += 1
                    tailIndex[1] += 1
            elif direction == "U":
                headIndex = [headIndex[0] - 1, headIndex[1]]

                if headIndex[0] <= 0:
                    board = [[Square() for _ in board[0]]] + board
                    headIndex[0] += 1
                    tailIndex[0] += 1
            elif direction == "D":
                headIndex = [headIndex[0] + 1, headIndex[1]]

                if headIndex[0] >= len(board):
                    board = board + [[Square() for _ in board[0]]]

            updateIndexes()

    return sum([len([1 for s in b if s.visited]) for b in board])


def problemTwo():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    board = [[Square(True, True)]]
    knots = [[0, 0] for _ in range(10)]

    def updateIndexes():
        nonlocal board, knots
        for i in range(1, len(knots)):
            headIndex = knots[i - 1]
            tailIndex = knots[i]

            if headIndex[0] == tailIndex[0]:
                if headIndex[1] - tailIndex[1] > 1:
                    tailIndex[1] += 1
                elif tailIndex[1] - headIndex[1] > 1:
                    tailIndex[1] -= 1
            elif headIndex[1] == tailIndex[1]:
                if headIndex[0] - tailIndex[0] > 1:
                    tailIndex[0] += 1
                elif tailIndex[0] - headIndex[0] > 1:
                    tailIndex[0] -= 1
            elif (
                abs(headIndex[0] - tailIndex[0]) != 1
                or abs(headIndex[1] - tailIndex[1]) != 1
            ):
                horizontal = 1
                vertical = 1

                if headIndex[0] < tailIndex[0]:
                    vertical = -1
                if headIndex[1] < tailIndex[1]:
                    horizontal = -1

                tailIndex[0] += vertical
                tailIndex[1] += horizontal

        board[knots[9][0]][knots[9][1]].visited = True

    for line in lines:
        [direction, numMoves] = line.split(" ")
        numMoves = int(numMoves)

        for _ in range(numMoves):
            if direction == "R":
                knots[0] = [knots[0][0], knots[0][1] + 1]

                if knots[0][1] >= len(board[0]):
                    board = [b + [Square()] for b in board]
            elif direction == "L":
                knots[0] = [knots[0][0], knots[0][1] - 1]

                if knots[0][1] < 0:
                    board = [[Square()] + b for b in board]

                    for knot in knots:
                        knot[1] += 1
            elif direction == "U":
                knots[0] = [knots[0][0] - 1, knots[0][1]]

                if knots[0][0] <= 0:
                    board = [[Square() for _ in board[0]]] + board

                    for knot in knots:
                        knot[0] += 1
            elif direction == "D":
                knots[0] = [knots[0][0] + 1, knots[0][1]]

                if knots[0][0] >= len(board):
                    board = board + [[Square() for _ in board[0]]]

            updateIndexes()

    return sum([len([1 for s in b if s.visited]) for b in board])


class Square:
    def __init__(self, visited=False, start=False):
        self.visited = visited
        self.start = start

    def __str__(self):
        return "s" if self.start else "#" if self.visited else "."


print(problemTwo())
