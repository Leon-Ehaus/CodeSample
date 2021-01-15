def partOne(inputStringArr) -> int:
    ruleList = []
    for x in inputStringArr:
        singleRule = isollate(x)
        ruleList = ruleList + [singleRule[::2]]

    possibleContainers = ["shiny gold bag"]
    for container in possibleContainers:
        possibleContainers = searchForTransitiveContainer(
            possibleContainers, ruleList, container)

    # -1 because shiny gold bag is in the possibleContainers but not a vaild answer
    return len(possibleContainers)-1


def searchForTransitiveContainer(visitedBags, ruleList, bag) -> list:
    """searches in ruleList for bags wich can contain the bag direktly and arent visited already."""
    for x in ruleList:
        if bag in x[1:]:
            if x[0] not in visitedBags:
                visitedBags.append(x[0])

    return visitedBags


def isollate(lineString):
    """splis the lineString into an array with the number and bag types"""
    lineString = lineString.replace("bags", "bag")
    lineString = lineString.replace(".", "")
    lineStringArr = lineString.split("contain")
    root = lineStringArr[0].strip()
    lineStringArr = [x.strip() for x in lineStringArr[1].split(",")]
    leafList = []
    for x in lineStringArr:
        leafList = leafList + [x[0]]+[x[2:]]

    return [root] + leafList


def partTwo(inputStringArr) -> int:
    return 0


with open('AdventOfCode20/Day7/inputDay7.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
