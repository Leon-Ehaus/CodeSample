def partOne(inputStringArr)-> int:
    countValid = 0
    for x in inputStringArr:
        if checkIfVaild(x):
            countValid += 1
    return countValid

def checkIfVaild(inputString)-> bool:
    splitString = inputString.split(":")
    passwordString = splitString[1].strip()
    relevantChar = splitString[0][-1]
    charCount = splitString[0][:-2].split("-")
    charCount = list(map(int, charCount))
    count = passwordString.count(relevantChar)
    return (count >= charCount[0] and count <= charCount[1])



with open('AdventOfCode20/input.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]
print(partOne(inputArr))