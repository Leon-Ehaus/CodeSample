def partOne(inputMap) -> int:
    mapsize = len(inputMap[0])
    treeCount = 0
    for i, x in enumerate(inputMap):
        if "#" == x[(i*3) % mapsize]:
            treeCount += 1
    return treeCount


def partTwo(inputMap) -> int:
    a = partTwoHelper(inputMap, 1)
    b = partTwoHelper(inputMap, 3)
    c = partTwoHelper(inputMap, 5)
    d = partTwoHelper(inputMap, 7)
    inputMap = inputMap[::2]
    e = partTwoHelper(inputMap, 1)
    return a*b*c*d*e


def partTwoHelper(inputMap, offset) -> int:
    mapsize = len(inputMap[0])
    treeCount = 0
    for i, x in enumerate(inputMap):
        if "#" == x[(i*offset) % mapsize]:
            treeCount += 1
    return treeCount


with open('AdventOfCode20/input.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]
print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
