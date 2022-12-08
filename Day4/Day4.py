def problemOne():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    numFullContained = 0
    for pair in input.splitlines():
        [elf1, elf2] = pair.split(",")
        [elf1min, elf1max] = [int(e) for e in elf1.split("-")]
        [elf2min, elf2max] = [int(e) for e in elf2.split("-")]

        if (elf1min <= elf2min and elf1max >= elf2max) or (
            elf2min <= elf1min and elf2max >= elf1max
        ):
            numFullContained += 1

    return numFullContained


def problemTwo():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() if line.rstrip() != "" else "#" for line in f]

    numOverlap = 0
    for pair in lines:
        [elf1, elf2] = pair.split(",")
        [elf1min, elf1max] = [int(e) for e in elf1.split("-")]
        [elf2min, elf2max] = [int(e) for e in elf2.split("-")]

        if (elf1min <= elf2min and elf2min <= elf1max) or (
            elf2min <= elf1min and elf1min <= elf2max
        ):
            numOverlap += 1

    return numOverlap


print(problemTwo())
