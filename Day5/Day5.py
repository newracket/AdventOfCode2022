import re


def problemOne():
    with open("input.txt", "r") as f:
        input = f.read()

    [stacksLines, instructionsLines] = input.split("\n\n")
    stacks = []

    for stack in reversed(stacksLines.split("\n")):
        if len(stacks) == 0:
            stacks = [[] for _ in stack.split("   ")]
        else:
            parsedStack = stack.replace("    ", " ")
            items = parsedStack.split(" ")

            for i, item in enumerate(items):
                if len(item) > 0:
                    stacks[i].append(item[1:-1])

    for instruction in instructionsLines.split("\n"):
        [numMove, moveFrom, moveTo] = [
            int(e) for e in re.findall(r"(\d+)", instruction)
        ]

        for _ in range(numMove):
            stacks[moveTo - 1].append(stacks[moveFrom - 1].pop())

    return "".join([e.pop() for e in stacks])


def problemTwo():
    with open("input.txt", "r") as f:
        input = f.read()

    [stacksLines, instructionsLines] = input.split("\n\n")
    stacks = []

    for stack in reversed(stacksLines.split("\n")):
        if len(stacks) == 0:
            stacks = [[] for _ in stack.split("   ")]
        else:
            parsedStack = stack.replace("    ", " ")
            items = parsedStack.split(" ")

            for i, item in enumerate(items):
                if len(item) > 0:
                    stacks[i].append(item[1:-1])

    for instruction in instructionsLines.split("\n"):
        [numMove, moveFrom, moveTo] = [
            int(e) for e in re.findall(r"(\d+)", instruction)
        ]

        stacks[moveTo - 1].extend(stacks[moveFrom - 1][-numMove:])
        stacks[moveFrom - 1] = stacks[moveFrom - 1][:-numMove]

    return "".join([e.pop() for e in stacks])


print(problemOne())
