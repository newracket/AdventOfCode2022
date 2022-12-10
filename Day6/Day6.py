def problemOne():
    with open("input.txt", "r") as f:
        input = f.read()

    numLetters = 4
    for i in range(numLetters - 1, len(input)):
        letters = list(input[i - numLetters : i])
        lettersSet = set(letters)

        if len(lettersSet) == numLetters:
            return i


def problemTwo():
    with open("input.txt", "r") as f:
        input = f.read()

    numLetters = 14
    for i in range(numLetters - 1, len(input)):
        letters = list(input[i - numLetters : i])
        lettersSet = set(letters)

        if len(lettersSet) == numLetters:
            return i


print(problemTwo())
