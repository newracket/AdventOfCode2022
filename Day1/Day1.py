def problemOne():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    elves = input.split("\n\n")
    elvesCaloriesSplit = [[int(b) for b in a.split("\n")] for a in elves]
    elvesCalories = map(sum, elvesCaloriesSplit)

    return max(elvesCalories)


def problemTwo():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    elves = input.split("\n\n")
    elvesCaloriesSplit = [[int(b) for b in a.split("\n")] for a in elves]
    elvesCalories = map(sum, elvesCaloriesSplit)

    topCalories = [-1, -1, -1]
    for v in elvesCalories:
        for i in range(len(topCalories), 0, -1):
            if v > topCalories[i - 1]:
                topCalories[i - 1] = v
                break

    return sum(topCalories)


print(problemTwo())
