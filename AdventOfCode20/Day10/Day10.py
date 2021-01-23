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
    inputIntArr = sorted(inputIntArr)
    inputIntArr = inputIntArr + [inputIntArr[-1] + 3]
    previous = 0
    totalPermutationCount = 1
    currentPermutationArr = []
    previousDouble = False
    for jumper in inputIntArr:
        if (jumper - previous) == 1:
            currentPermutationArr = currentPermutationArr + [1]
            previousDouble = False
        elif (jumper - previous) == 2 and not previousDouble:
            currentPermutationArr = currentPermutationArr + [2]
            previousDouble = True
        else:
            totalPermutationCount *= calcPermutation(currentPermutationArr)
            currentPermutationArr = [jumper - previous]
            previousDouble = False

        previous = jumper

    return totalPermutationCount


def calcPermutation(intArr) -> int:
    singleJumpCount = intArr.count(1)
    doubleJumpCount = intArr.count(2)
    print(intArr.count(3))
    if doubleJumpCount is not 0:
        print(intArr)
    elif singleJumpCount is not 0:
        if singleJumpCount == 2:
            return 2
        elif singleJumpCount == 3:
            return 4
        elif singleJumpCount == 4:
            return 7
    print(intArr)
    return 1


with open('AdventOfCode20/Day10/inputDay10.txt') as f:
    inputArr = f.readlines()

inputArr = [int(x.strip()) for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
