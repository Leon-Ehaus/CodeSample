
def partOne(inputStringArr, target)-> (int,int):
    inputIntArr = [int(num) for num in inputStringArr]
    inputIntArr.sort()

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
            print("No matching numbers for the target found")
            break

    return (firstSummand,secondSummand)







with open('AdventOfCode20/input.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]

print(partOne(inputArr, 2020))