def partOne(inputString) -> int:
    groupList = inputString.split("\n\n")
    count = 0
    for x in groupList:
        count += countQuestions(x)
    return count

def countQuestions(groupString)-> int:
    """Counts how many different characters are in groupString"""
    groupString = groupString.replace("\n","")
    count = 0
    while len(groupString)>0:
        x = groupString[0]
        groupString = groupString.replace(x,"")
        count += 1
    return count

def partTwo(inputString) -> int:
    return 0


with open('AdventOfCode20/Day6/inputDay6.txt') as f:
    inputString = f.read()



print("Solution part one: ", partOne(inputString),
      "\nSolution part two: ", partTwo(inputString))
