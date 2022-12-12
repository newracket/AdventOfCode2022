def problemOne():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    trees = [[{"height": int(t), "visible": False} for t in line] for line in lines]
    horizontalListsToTraverse = [trees, [list(reversed(t)) for t in trees]]
    for listToTraverse in horizontalListsToTraverse:
        for treeLine in listToTraverse:
            largest = -1
            for tree in treeLine:
                height = int(tree["height"])
                if height > largest:
                    largest = height
                    tree["visible"] = True

    verticalListsToTraverse = [trees, list(reversed(trees))]
    for listToTraverse in verticalListsToTraverse:
        for col in range(len(listToTraverse[0])):
            largest = -1
            for row in range(len(listToTraverse)):
                tree = listToTraverse[row][col]
                height = int(tree["height"])
                if height > largest:
                    largest = height
                    tree["visible"] = True

    visibleTrees = [[t for t in treeLine if t["visible"] == True] for treeLine in trees]
    numVisibleTrees = sum([len(t) for t in visibleTrees])
    return numVisibleTrees


def getScore(trees, row, col):
    if row == 0 or col == 0 or row == len(trees) - 1 or col == len(trees[row]) - 1:
        return 0

    tree = trees[row][col]

    # Check left
    leftCount = 0
    for i in range(col - 1, -1, -1):
        leftCount += 1
        if tree["height"] <= trees[row][i]["height"]:
            break

    # Check right
    rightCount = 0
    for i in range(col + 1, len(trees[row])):
        rightCount += 1
        if tree["height"] <= trees[row][i]["height"]:
            break

    # Check up
    upCount = 0
    for i in range(row - 1, -1, -1):
        upCount += 1
        if tree["height"] <= trees[i][col]["height"]:
            break

    # Check down
    downCount = 0
    for i in range(row + 1, len(trees)):
        downCount += 1
        if tree["height"] <= trees[i][col]["height"]:
            break

    return leftCount * rightCount * upCount * downCount


def problemTwo():
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    trees = [[{"height": int(t), "score": 0} for t in line] for line in lines]
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            tree = trees[row][col]
            tree["score"] = getScore(trees, row, col)

    return max([max([t["score"] for t in treeLine]) for treeLine in trees])


print(problemTwo())
