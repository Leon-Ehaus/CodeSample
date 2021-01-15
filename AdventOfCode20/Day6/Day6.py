def partOne(inputString) -> int:
    groupList = inputString.split("\n\n")
    count = 0
    for x in groupList:
        count += countQuestions(x)
    return count


def countQuestions(groupString) -> int:
    """Counts how many different characters are in groupString"""
    groupString = groupString.replace("\n", "")
    count = 0
    while len(groupString) > 0:
        x = groupString[0]
        groupString = groupString.replace(x, "")
        count += 1
    return count


def partTwo(inputString) -> int:
    groupList = inputString.split("\n\n")
    count = 0
    for x in groupList:
        count += countAswered(x)
    return count


def countAswered(groupString) -> int:
    """Counts how many different characters are present in all lines of the groupString"""
    groupList = groupString.split("\n")
    #groupList = groupList.sort(lambda x,y: cmp(len(x), len(y)))
    count = 0
    while len(groupList[0]) > 0:
        x = groupList[0][0]
        for i, person in enumerate(groupList):
            if x not in person:
                break
            groupList[i] = groupList[i].replace(x, "")
            if i == len(groupList)-1:
                count += 1
    return count


with open('AdventOfCode20/Day6/inputDay6.txt') as f:
    inputString = f.read()


print("Solution part one: ", partOne(inputString),
      "\nSolution part two: ", partTwo(inputString))
