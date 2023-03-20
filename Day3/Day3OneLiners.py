def problemOne(): return sum([ord(item) - 96 if item.islower() else ord(item) - 38 for item in [list(set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:])))[0] for line in open("input.txt", "r").read().splitlines()]])

def problemTwo(): return sum([ord(item) - 96 if item.islower() else ord(item) - 38 for item in [list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0] for group in [[line for line in open("input.txt", "r").read().splitlines()][i:i + 3] for i in range(0, len([line for line in open("input.txt", "r").read().splitlines()]), 3)]]])

print(problemOne())
print(problemTwo())