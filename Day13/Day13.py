from enum import Enum
from functools import cmp_to_key
from json import loads


def problemOne():
    with open("input.txt", "r") as f:
        data = f.read()

    class Greater(Enum):
        LEFT = 1
        RIGHT = -1
        NEITHER = 0

    def compareLists(left: list[any], right: list[any]) -> Greater:
        left = left.copy()
        right = right.copy()
        while len(left) > 0 and len(right) > 0:
            if isinstance(left[0], list) and isinstance(right[0], list):
                nestedResult = compareLists(left[0], right[0])

                if nestedResult == Greater.NEITHER:
                    left.pop(0)
                    right.pop(0)
                    continue

                return nestedResult
            elif isinstance(left[0], list):
                right[0] = [right[0]]
                continue
            elif isinstance(right[0], list):
                left[0] = [left[0]]
                continue
            else:
                if left[0] < right[0]:
                    return Greater.LEFT
                elif left[0] == right[0]:
                    left.pop(0)
                    right.pop(0)
                    continue
                else:
                    return Greater.RIGHT

        if len(left) == 0 and len(right) == 0:
            return Greater.NEITHER
        elif len(left) == 0:
            return Greater.LEFT
        elif len(right) == 0:
            return Greater.RIGHT

    # Problem One
    # pairs = [[loads(e) for e in d.splitlines()] for d in data.split("\n\n")]
    # sum = 0
    # for i, pair in enumerate(pairs, start=1):
    #     [leftList, rightList] = pair
    #     result = compareLists(leftList, rightList)
    #
    #     if result == Greater.LEFT:
    #         sum += i
    #
    # return sum

    # Problem Two
    packets = [loads(e) for e in data.replace("\n\n", "\n").splitlines()] + [
        [[2]], [[6]]]
    packets.sort(key=cmp_to_key(lambda e1, e2: compareLists(e1, e2).value),
                 reverse=True)

    twoLocation = packets.index([[2]]) + 1
    sixLocation = packets.index([[6]]) + 1

    return twoLocation * sixLocation


print(problemOne())
