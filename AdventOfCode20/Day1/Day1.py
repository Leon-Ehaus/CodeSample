
def partOne(inputStringArr) -> int:
    inputIntArr = [int(num) for num in inputStringArr]
    inputIntArr.sort()
    sumPair = findSumPairForTarget(inputIntArr, 2020)
    return sumPair[0] * sumPair[1]


def partTwo(inputStringArr) -> int:
    inputIntArr = [int(num) for num in inputStringArr]
    inputIntArr.sort()
    for i in range(len(inputIntArr)):
        target = 2020 - inputIntArr[i]
        sumPair = findSumPairForTarget(
            inputIntArr[:i] + inputIntArr[i+1:], target)
        if sumPair != (-1, -1):
            return inputIntArr[i] * sumPair[0] * sumPair[1]



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


with open('AdventOfCode20/Day1/inputDay1.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]

print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
