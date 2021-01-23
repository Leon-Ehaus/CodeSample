def partOne(inputStringArr) -> int:
    oldLayout = []
    while oldLayout != inputStringArr:
        oldLayout = inputStringArr
        inputStringArr = step(inputStringArr)

    ocuupiedCount = 0

    for line in inputStringArr:
        ocuupiedCount += line.count("#")

    return ocuupiedCount


def step(seatLayout) -> list:
    """returns the new seatLayout after applying the rules once"""
    newLayout = []
    for i, line in enumerate(seatLayout):
        newLine = []
        for j, cell in enumerate(line):
            if cell == "L":
                newLine = newLine + [ruleOne(i, j, seatLayout)]
            elif cell == "#":
                newLine = newLine + [ruleTwo(i, j, seatLayout)]
            else:
                newLine = newLine + ["."]
        newLayout = newLayout + [newLine]
    return newLayout


def ruleOne(rowNr, colNr, seatLayout) -> str:
    """returns the new value of the specified location if rule one is applied"""
    for i in range( rowNr - 1, rowNr + 2):
        for j in range(colNr - 1, colNr + 2):
            if i < 0 or j < 0 or i >= len(seatLayout) or j >= len(seatLayout[0]):
                continue
            if seatLayout[i][j] == "#":
                return "L"
    return "#"


def ruleTwo(rowNr, colNr, seatLayout) -> str:
    """returns the new value of the specified location if rule two is applied"""
    ocuupiedCount = 0
    for i in range( rowNr - 1, rowNr + 2):
        for j in range(colNr - 1, colNr + 2):
            if i < 0 or j < 0 or i >= len(seatLayout) or j >= len(seatLayout[0]):
                continue
            if seatLayout[i][j] == "#":
                ocuupiedCount += 1
    
    if ocuupiedCount <= 4 :
        return "#"
    else:
        return "L"


def partTwo(inputArr) -> int:

    return 0


with open('AdventOfCode20/Day11/inputDay11.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]




print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
