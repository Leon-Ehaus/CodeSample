import math


def partOne(inputStringArr):
    listID = [calcPassID(x) for x in inputStringArr]
    listID.sort()
    return listID[-1]


def calcPassID(String) -> int:
    result = 0
    String = String.replace("B", "1")
    String = String.replace("F", "0")
    String = String.replace("R", "1")
    String = String.replace("L", "0")
    return int(String, 2)


with open('AdventOfCode20/input.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]


print("Solution part one: ", partOne(inputArr), "\nSolution part two: ", 0)
