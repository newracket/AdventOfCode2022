import re
import time


def problemOne():
    with open("input.txt", "r") as f:
        data = f.read()

    instructions = data.splitlines()
    maxX = maxY = -1e7
    minX = minY = 1e7

    for instruction in instructions:
        [sX, sY, bX, bY] = [int(e) for e in
                            re.findall(r"([-\d]+)", instruction)]
        maxX = max(maxX, sX, bX)
        maxY = max(maxY, sY, bY)
        minX = min(minX, sX, bX)
        minY = min(minY, sY, bY)

    rowNum = 2000000
    expandValue = 1000000
    minX -= expandValue
    maxX += expandValue

    row = ["." for _ in range(maxX - minX + 1)]

    def identifyImpossibles(sensorX, sensorY, beaconX, beaconY):
        distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)
        xLen = (distance - abs(rowNum - sensorY)) * 2 + 1
        startX = sensorX - (distance - abs(rowNum - sensorY))

        for j in range(startX, startX + xLen):
            if 0 <= j - minX < len(row) and row[j - minX] == ".":
                row[j - minX] = "#"

    for instruction in instructions:
        [sX, sY, bX, bY] = [int(e) for e in
                            re.findall(r"([-\d]+)", instruction)]

        if sY == rowNum:
            row[sX - minX] = "S"
        if bY == rowNum:
            row[bX - minX] = "B"

        identifyImpossibles(sX, sY, bX, bY)

    # print(board.getRow(rowNum))
    print(row.count("#"))


def problemTwo():
    with open("input.txt", "r") as f:
        data = f.read()

    instructions = data.splitlines()

    def man(xy1, xy2):
        return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

    scanners = set()
    pos, neg = set(), set()
    for instruction in instructions:
        print(instruction)
        [sX, sY, bX, bY] = [int(e) for e in
                            re.findall(r"([-\d]+)", instruction)]
        r = man((sX, sY), (bX, bY))
        scanners.add((sX, sY, r))

        pos.add(sY - sX + r + 1)
        pos.add(sY - sX - r - 1)
        neg.add(sY + sX + r + 1)
        neg.add(sY + sX - r - 1)

    tuningFreqNum = 4_000_000
    bound = tuningFreqNum
    for p in pos:
        for n in neg:
            inter = ((n - p) // 2, (n + p) // 2)
            if all(0 < c < bound for c in inter):
                if all(man(inter, s) > s[2] for s in scanners):
                    print(inter)
                    print(inter[0] * tuningFreqNum + inter[1])
                    break


start = time.time()
# problemOne()
problemTwo()

print(time.time() - start)
