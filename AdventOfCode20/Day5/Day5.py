import math


def partOne(inputStringArr) -> int:
    listID = [calcPassID(x) for x in inputStringArr]
    listID.sort()
    return listID[-1]


def calcPassID(passString) -> int:
    """calculates the ID of the passString according to the problem description"""
    passString = passString.replace("B", "1")
    passString = passString.replace("F", "0")
    passString = passString.replace("R", "1")
    passString = passString.replace("L", "0")
    return int(passString, 2)


def partTwo(inputStringArr) -> int:
    listID = [calcPassID(x) for x in inputStringArr]
    listID.sort()
    lastID = listID[0] - 1

    for x in listID:
        if x != lastID + 1:
            return lastID + 1
        lastID = x

    return 0


with open('AdventOfCode20/Day5/inputDay5.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
