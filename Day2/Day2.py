def problemOne():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    valuesDict = {
        "A": "R",
        "B": "P",
        "C": "S",
        "X": "R",
        "Y": "P",
        "Z": "S",
    }
    scoreDict = {
        "R": 1,
        "P": 2,
        "S": 3,
    }

    score = 0
    for move in input.split("\n"):
        [opponentMoveSymbol, myMoveSymbol] = move.split(" ")
        [opponentMove, myMove] = [
            valuesDict[opponentMoveSymbol],
            valuesDict[myMoveSymbol],
        ]

        if myMove == opponentMove:
            score += scoreDict[myMove] + 3
            continue

        win = (
            myMove == "R"
            and opponentMove == "S"
            or myMove == "P"
            and opponentMove == "R"
            or myMove == "S"
            and opponentMove == "P"
        )
        if win:
            score += scoreDict[myMove] + 6
        else:
            score += scoreDict[myMove]

    return score


def problemTwo():
    f = open("input.txt", "r")
    input = f.read()
    f.close()

    valuesDict = {
        "A": "R",
        "B": "P",
        "C": "S",
    }
    scoreDict = {
        "R": 1,
        "P": 2,
        "S": 3,
    }

    score = 0
    for move in input.split("\n"):
        [opponentMoveSymbol, myMoveSymbol] = move.split(" ")
        opponentMove = valuesDict[opponentMoveSymbol]

        if myMoveSymbol == "Y":
            score += scoreDict[opponentMove] + 3
            continue
        elif myMoveSymbol == "X":
            match opponentMove:
                case "R":
                    score += scoreDict["S"]
                case "P":
                    score += scoreDict["R"]
                case "S":
                    score += scoreDict["P"]
        else:
            match opponentMove:
                case "R":
                    score += scoreDict["P"] + 6
                case "P":
                    score += scoreDict["S"] + 6
                case "S":
                    score += scoreDict["R"] + 6

    return score


print(problemTwo())
