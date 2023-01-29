import re


def problemOne():
    with open("input.txt", "r") as f:
        data = f.read()

    monkeyInstructions = data.split("\n\n")
    monkeys = []

    for monkeyInstruction in monkeyInstructions:
        instructions = monkeyInstruction.split("\n")

        startingItemsText = re.findall(r"Starting items: (.*)", instructions[1])[0]
        startingItems = [int(e) for e in startingItemsText.split(", ")]
        operationText = instructions[2].split(" = ")[1]
        divisibleNum = int(re.findall(r"(\d+)", instructions[3])[0])
        trueMonk = int(re.findall(r"(\d+)", instructions[4])[0])
        falseMonk = int(re.findall(r"(\d+)", instructions[5])[0])

        monkeys.append(
            Monkey(startingItems, operationText, divisibleNum, trueMonk, falseMonk)
        )

    for _ in range(0, 20):
        for monkey in monkeys:
            monkey.actionProblemOne(monkeys)

    inspectedNums = [monkey.inspectedNum for monkey in monkeys]
    max1 = max2 = -1

    for inspectedNum in inspectedNums:
        if inspectedNum > max1:
            max2 = max1
            max1 = inspectedNum
        elif inspectedNum > max2:
            max2 = inspectedNum

    return max1 * max2


def problemTwo():
    with open("input.txt", "r") as f:
        data = f.read()

    monkeyInstructions = data.split("\n\n")
    monkeys = []

    for monkeyInstruction in monkeyInstructions:
        instructions = monkeyInstruction.split("\n")

        startingItemsText = re.findall(r"Starting items: (.*)", instructions[1])[0]
        startingItems = [int(e) for e in startingItemsText.split(", ")]
        operationText = instructions[2].split(" = ")[1]
        divisibleNum = int(re.findall(r"(\d+)", instructions[3])[0])
        trueMonk = int(re.findall(r"(\d+)", instructions[4])[0])
        falseMonk = int(re.findall(r"(\d+)", instructions[5])[0])

        monkeys.append(
            Monkey(startingItems, operationText, divisibleNum, trueMonk, falseMonk)
        )

    for i in range(0, 10000):
        print(i)
        for monkey in monkeys:
            monkey.actionProblemTwo(monkeys)

    inspectedNums = [monkey.inspectedNum for monkey in monkeys]
    max1 = max2 = -1

    for inspectedNum in inspectedNums:
        if inspectedNum > max1:
            max2 = max1
            max1 = inspectedNum
        elif inspectedNum > max2:
            max2 = inspectedNum

    return max1 * max2


class Monkey:
    def __init__(self, items, operationText, divisibleNum, trueMonk, falseMonk):
        self.operationFunction = None
        self.items = items
        self.operationText = operationText
        self.divisibleNum = divisibleNum
        self.trueMonk = trueMonk
        self.falseMonk = falseMonk
        self.inspectedNum = 0

        self.setOperationFunction()

    def setOperationFunction(self):
        def operationFunction(old):
            [num1, operation, num2] = self.operationText.split(" ")

            if num1 == "old":
                num1 = old
            else:
                num1 = int(num1)

            if num2 == "old":
                num2 = old
            else:
                num2 = int(num2)

            if operation == "+":
                return num1 + num2
            elif operation == "*":
                return num1 * num2

        self.operationFunction = operationFunction

    def addItem(self, item):
        self.items.append(item)

    def actionProblemOne(self, monkeys):
        while len(self.items) > 0:
            self.inspectedNum += 1
            worryLevel = self.operationFunction(self.items.pop(0))
            worryLevel //= 3

            if worryLevel % self.divisibleNum == 0:
                monkeys[self.trueMonk].addItem(worryLevel)
            else:
                monkeys[self.falseMonk].addItem(worryLevel)

    def actionProblemTwo(self, monkeys):
        while len(self.items) > 0:
            self.inspectedNum += 1
            worryLevel = self.operationFunction(self.items.pop(0))

            if worryLevel % self.divisibleNum == 0:
                monkeys[self.trueMonk].addItem(worryLevel)
            else:
                monkeys[self.falseMonk].addItem(worryLevel)


print(problemTwo())
