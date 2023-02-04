import math


def problemOne():
    with open("input.txt", "r") as f:
        data = f.read()

    lines = data.splitlines()
    maxY = 0
    minX = math.inf
    maxX = 0

    for line in lines:
        instructions = line.split(" -> ")
        minX = min([minX] + [int(e.split(",")[0]) for e in instructions])
        maxY = max([maxY] + [int(e.split(",")[1]) for e in instructions])
        maxX = max([maxX] + [int(e.split(",")[0]) for e in instructions])

    board = Board(minX, maxX, maxY)

    def setRangeToRock(start, end):
        [startX, startY] = [int(e) for e in start.split(",")]
        [endX, endY] = [int(e) for e in end.split(",")]

        [startX, endX] = sorted([startX, endX])
        [startY, endY] = sorted([startY, endY])

        if startX == endX:
            for y in range(startY, endY + 1):
                board.set(startX, y, "#")
        elif startY == endY:
            for x in range(startX, endX + 1):
                board.set(x, startY, "#")

    for line in lines:
        instructions = line.split(" -> ")
        current = instructions.pop(0)

        while len(instructions) > 0:
            setRangeToRock(current, instructions[0])
            current = instructions.pop(0)

    board.expand()
    board.problemTwo()

    numSand = 0
    currentX = 500
    currentY = 0
    while True:
        if board.get(currentX, currentY + 1) == ".":
            currentY += 1
        elif board.get(currentX - 1, currentY + 1) == ".":
            currentX -= 1
            currentY += 1
        elif board.get(currentX + 1, currentY + 1) == ".":
            currentX += 1
            currentY += 1
        else:
            if board.get(currentX, currentY + 1) == " ":
                break

            board.set(currentX, currentY, "o")
            numSand += 1

            if currentX == 500 and currentY == 0:
                break

            currentX = 500
            currentY = 0

    print(board)
    print(numSand)


class Board:
    def __init__(self, minX, maxX, maxY):
        self.minX = minX
        self.maxX = maxX
        self.maxY = maxY

        self.board = [["." for _ in range(maxX - minX + 1)] for _ in
                      range(maxY + 1)]

    def get(self, x, y):
        if not self.inBoard(x, y):
            return " "
        return self.board[y][x - self.minX]

    def set(self, x, y, value):
        if self.inBoard(x, y):
            self.board[y][x - self.minX] = value

    def inBoard(self, x, y):
        return self.minX <= x <= self.maxX and 0 <= y <= self.maxY

    def expand(self):
        self.minX -= 1
        self.maxX += 1
        self.board = [["."] + e + ["."] for e in self.board]

        self.maxY += 1
        self.board.append(["." for _ in range(self.maxX - self.minX + 1)])

    def problemTwo(self):
        oldMinX = self.minX
        self.minX = 0
        self.maxX += oldMinX
        self.board = [
            ["." for _ in range(oldMinX)] + e + ["." for _ in range(oldMinX)]
            for e in self.board]

        self.maxY += 1
        self.board.append(["#" for _ in range(self.maxX - self.minX + 1)])

    def __str__(self):
        return "\n".join(["".join(e) for e in self.board])


problemOne()
