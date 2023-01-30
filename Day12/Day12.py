from datetime import datetime


def problemOne():
    with open("input.txt", "r") as f:
        data = f.read()

    data = data.splitlines()
    board = [[ord(e) for e in list(d)] for d in data]

    startXOne = 0
    startYOne = 0
    endXOne = 0
    endYOne = 0

    for rowIndex in range(len(board)):
        for colIndex, item in enumerate(board[rowIndex]):
            if item == 83:
                startXOne = colIndex
                startYOne = rowIndex
            elif item == 69:
                endXOne = colIndex
                endYOne = rowIndex

    board[startYOne][startXOne] = ord('a')
    board[endYOne][endXOne] = ord('z')

    def findFastest(startX, startY):
        visited = set()
        unvisited = set()
        distances = {
            (startX, startY): 0
        }

        for row in range(len(board)):
            for col in range(len(board[row])):
                current = (col, row)
                unvisited.add(current)

                # if current not in distances:
                #     distances[current] = 1e7

        def getNeighbors(x, y):
            neighbors = []
            if x > 0:
                neighbors.append((y, x - 1))
            if x < len(board) - 1:
                neighbors.append((y, x + 1))
            if y > 0:
                neighbors.append((y - 1, x))
            if y < len(board[0]) - 1:
                neighbors.append((y + 1, x))
            return neighbors

        def getMinDistance():
            minDistance = 1e8
            minCoord = None

            for coord in unvisited:
                curr = distances.get(coord)

                if curr is not None and curr < minDistance:
                    minDistance = curr
                    minCoord = coord

            return minCoord

        while len(unvisited) > 0:
            current = getMinDistance()
            if len(distances) == 1:
                current = (startX, startY)

            if current is None:
                break

            unvisited.remove(current)
            visited.add(current)

            currentValue = board[current[1]][current[0]]
            for neighbor in getNeighbors(current[1], current[0]):
                neighborValue = board[neighbor[1]][neighbor[0]]

                if neighborValue - currentValue > 1:
                    continue

                newDistance = distances[current] + 1
                if neighbor not in distances or (
                        newDistance < distances[neighbor]):
                    distances[neighbor] = newDistance

        shortestPath = distances.get((endXOne, endYOne))
        if shortestPath is None:
            return 1e7

        return shortestPath

    time = datetime.now().timestamp()
    # Problem One
    # print(findFastest(startXOne, startYOne))

    # Problem Two
    minSteps = 1e7
    i = 0
    for rowIndex in range(len(board)):
        for colIndex, item in enumerate(board[rowIndex]):
            if item == ord('a'):
                steps = findFastest(colIndex, rowIndex)
                minSteps = min(minSteps, steps)
                i += 1

    print(minSteps)
    print(datetime.now().timestamp() - time)

    # print(findFastest(19, 0))


problemOne()
