def problemOne():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    x = 1
    cycles = 0
    totalSignalStrength = 0
    cyclesToNote = [20, 60, 100, 140, 180, 220]
    for line in lines:
        if line == "noop":
            cycles += 1
            continue

        num = int(line.split(" ")[1])
        cycles += 2
        if len(cyclesToNote) > 0 and cycles >= cyclesToNote[0]:
            totalSignalStrength += cyclesToNote[0] * x
            cyclesToNote.pop(0)
        x += num

    return totalSignalStrength


def problemTwo():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    x = 1
    instructions = [{"instruction": l, "cycleNum": 0} for l in lines]
    board = [["." for i in range(0, 40)] for i in range(0, 6)]
    row = 0
    col = 0

    while len(instructions) > 0:
        currentInstruction = instructions[0]
        currentInstruction["cycleNum"] += 1
        spritePositions = [x - 1, x, x + 1]

        if col in spritePositions:
            board[row][col] = "#"

        if currentInstruction["instruction"] == "noop":
            instructions.pop(0)
        elif currentInstruction["cycleNum"] == 2:
            instructions.pop(0)

            num = int(currentInstruction["instruction"].split(" ")[1])
            x += num

        col += 1
        if col >= 40:
            col = 0
            row += 1

    for row in board:
        print("".join(row))


print(problemTwo())
