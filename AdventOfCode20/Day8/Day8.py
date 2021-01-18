def partOne(inputStringArr) -> int:
    pos = 0
    accumulator = 0
    visitedPositions = [0]
    while True:
        output = runLine(inputStringArr[pos],accumulator,pos)
        accumulator = output[0]
        pos = output[1]
        if pos in visitedPositions:
            break
        else:
            visitedPositions.append(pos)

    return accumulator


def runLine(lineString, accumulator, pos):
    """executes one line and returns new value of acc and new pos"""
    lineArr = lineString.split(" ")

    if lineArr[0] == "acc":
        accumulator = accumulator + int(lineArr[1])
    elif lineArr[0] == "jmp":
        return (accumulator, pos + int(lineArr[1]))
    
    return (accumulator , pos + 1)

def partTwo(inputStringArr) -> int:

    return 0


with open('AdventOfCode20/Day8/inputDay8.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
