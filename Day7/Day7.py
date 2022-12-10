def run():
    with open("input.txt", "r") as f:
        input = f.read()
        lines = input.splitlines()

    currentDirectory = rootDirectory = Directory("root")
    indexOffset = 0
    for commandIndex in range(input.count("$")):
        line = lines[commandIndex + indexOffset]

        isCommand = line.startswith("$")
        if isCommand:
            command = line[2:]
            if command.startswith("cd"):
                directoryName = command[3:]
                if directoryName == "/":
                    currentDirectory = rootDirectory
                elif directoryName == "..":
                    currentDirectory = currentDirectory.parent
                else:
                    for file in currentDirectory.files:
                        if file.name == directoryName:
                            currentDirectory = file
                            break
            elif command.startswith("ls"):
                for listIndex in range(commandIndex + indexOffset + 1, len(lines)):
                    listLine = lines[listIndex]
                    if listLine.startswith("$"):
                        break

                    if listLine.startswith("dir"):
                        directoryName = listLine[4:]
                        currentDirectory.addFile(
                            Directory(directoryName, currentDirectory)
                        )
                    else:
                        [size, name] = listLine.split(" ")
                        currentDirectory.addFile(File(name, size))
                    indexOffset += 1

    print(
        "Problem One: "
        + str(sum([e for e in rootDirectory.directorySizes() if e < 100000]))
    )

    requiredSpace = 70000000 - rootDirectory.totalSize()
    print(
        "Problem Two: "
        + str(
            min(
                [
                    e
                    for e in rootDirectory.directorySizes()
                    if e > (30000000 - requiredSpace)
                ]
            )
        )
    )


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []

    def addFile(self, file):
        self.files.append(file)

    def totalSize(self):
        return sum([e.totalSize() for e in self.files])

    def directorySizes(self):
        return [self.totalSize()] + sum(
            [e.directorySizes() for e in self.files if type(e) == Directory], []
        )

    def __str__(self):
        return "/" + self.name + "".join(["\n\t" + str(e) for e in self.files])


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def totalSize(self):
        return int(self.size)

    def __str__(self):
        return "\t" + self.name + " " + str(self.size)


run()
