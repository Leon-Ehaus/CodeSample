def partOne(inputIntArr) -> int:
    inputIntArr = sorted(inputIntArr)
    previous = 0
    singleJumpCount = 0
    trippleJumpCount = 1
    for jumper in inputIntArr:
        if (jumper - previous) == 1:
            singleJumpCount += 1
        elif (jumper - previous) == 3:
            trippleJumpCount += 1
        previous = jumper

    return singleJumpCount * trippleJumpCount



def partTwo(inputIntArr) -> int:

    return 0


with open('AdventOfCode20/Day10/inputDay10.txt') as f:
    inputArr = f.readlines()

inputArr = [int(x.strip()) for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
