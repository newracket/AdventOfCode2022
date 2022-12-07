def problemOne():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    commonItems = []
    for sack in input.splitlines():
        sack1 = sack[: len(sack) // 2]
        sack2 = sack[len(sack) // 2 :]

        for item in sack1:
            if item in sack2:
                commonItems.append(item)
                break

    sum = 0
    for item in commonItems:
        if item.islower():
            sum += ord(item) - 96
        else:
            sum += ord(item) - 64 + 26

    return sum


def problemTwo():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    commonItems = []
    sacks = input.splitlines()
    for sackIndex in range(0, len(sacks), 3):
        sack1 = sacks[sackIndex]
        sack2 = sacks[sackIndex + 1]
        sack3 = sacks[sackIndex + 2]

        for item in sack1:
            if item in sack2 and item in sack3:
                commonItems.append(item)
                break

    sum = 0
    for item in commonItems:
        if item.islower():
            sum += ord(item) - 96
        else:
            sum += ord(item) - 64 + 26

    return sum


print(problemTwo())
