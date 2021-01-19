
def partOne(inputIntArr) -> int:
    preambleLen = 25
    if len(inputIntArr) < preambleLen:
        return -1

    for index in range(preambleLen, len(inputIntArr)):
        relevantPreamble = sorted(inputIntArr[index - preambleLen:index])
        sumPair = findSumPairForTarget(relevantPreamble, inputIntArr[index])
        if sumPair == (-1, -1):
            return inputIntArr[index]
    return -1


# copied from Day1. Not imported to ease understanding of the problem solution
def findSumPairForTarget(inputIntArr, target) -> (int, int):
    """finds a pair of int values in a sorted list that add to the target"""
    lowerSearchBound = 0
    upperSearchBound = len(inputIntArr) - 1
    firstSummand = 0
    secondSummand = 0

    while True:
        firstSummand = inputIntArr[lowerSearchBound]
        secondSummand = inputIntArr[upperSearchBound]
        tmpSum = firstSummand + secondSummand

        if tmpSum < target:
            lowerSearchBound += 1
        elif tmpSum > target:
            upperSearchBound -= 1
        else:
            break

        if lowerSearchBound >= upperSearchBound:
            return (-1, -1)

    return (firstSummand, secondSummand)


def partTwo(inputIntArr) -> int:

    return 0


with open('AdventOfCode20/Day9/inputDay9.txt') as f:
    inputArr = f.readlines()

inputArr = [int(x.strip()) for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
