def partOne(inputStringArr) -> int:
    countValid = 0
    for x in inputStringArr:
        if checkIfVaildOne(x):
            countValid += 1
    return countValid


def checkIfVaildOne(inputString) -> bool:
    splitString = inputString.split(":")
    passwordString = splitString[1].strip()
    relevantChar = splitString[0][-1]
    charCount = splitString[0][:-2].split("-")
    charCount = list(map(int, charCount))
    count = passwordString.count(relevantChar)
    return (count >= charCount[0] and count <= charCount[1])


def partTwo(inputStringArr) -> int:
    countValid = 0
    for x in inputStringArr:
        if checkIfVaildTwo(x):
            countValid += 1
    return countValid


def checkIfVaildTwo(inputString):
    splitString = inputString.split(":")
    passwordString = splitString[1].strip()
    relevantChar = splitString[0][-1]
    charPos = splitString[0][:-2].split("-")
    charPos = list(map(int, charPos))
    return (relevantChar == passwordString[charPos[0]-1]) != (relevantChar == passwordString[charPos[1]-1])


with open('AdventOfCode20/input.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]
print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
