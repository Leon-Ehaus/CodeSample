def partOne(inputString) -> int:

    inputString = inputString.split("\n\n")
    countValid = 0
    for i, x in enumerate(inputString):
        passportString = x.replace("\n", " ")
        passportFields = passportString.split(" ")
        for index, line in enumerate(passportFields):
            passportFields[index] = line.split(":")[0]
        if(all(x in passportFields for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])):
            countValid += 1

    return countValid


def partTwo(inputString) -> int:

    inputStringList = inputString.split("\n\n")
    countValid = len(inputStringList)
    for i, x in enumerate(inputStringList):
        passportString = x.replace("\n", " ")
        passportFields = passportString.split(" ")
        passportFieldsIdentifier = passportFields.copy()

        for index, line in enumerate(passportFields):
            passportFields[index] = line.split(":")
            passportFieldsIdentifier[index] = line.split(":")[0]

        if all(x in passportFieldsIdentifier for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            for field in passportFields:
                if(not(keyCheck(field))):
                    countValid -= 1
                    break
        else:
            countValid -= 1

    return countValid


def keyCheck(field) -> bool:
    """checks if the field has a valid value according to the problem description"""
    return{
        'byr': intRangeCheck(field[1], 1920, 2002),
        'iyr': intRangeCheck(field[1], 2010, 2020),
        'eyr': intRangeCheck(field[1], 2020, 2030),
        'hgt': hgt(field[1]),
        'hcl': hcl(field[1]),
        'ecl': ecl(field[1]),
        'pid': pid(field[1]),
        'cid': True
    }.get(field[0], False)


def intRangeCheck(string, minVal, maxVal) -> bool:
    """checks if the int value in string is between (inclusive) minVal and maxVal"""
    try:
        return(minVal <= int(string) <= maxVal)
    except ValueError:
        return False


def hgt(string) -> bool:
    """checks if string is a vaild value of hgt according to the problem description"""
    stringEnd = string[-2:]
    if stringEnd == "cm":
        return intRangeCheck(string[:-2], 150, 193)
    elif stringEnd == "in":
        return intRangeCheck(string[:-2], 59, 76)
    else:
        return False


def hcl(string) -> bool:
    """checks if string is a vaild value of hcl according to the problem description"""
    if string[0] == '#':
        try:
            int(string[1:], 16)
            return True
        except ValueError:
            return False
    return False


def ecl(string) -> bool:
    """checks if string is a vaild value of ecl according to the problem description"""
    return string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid(string) -> bool:
    """checks if string is a vaild value of pid according to the problem description"""
    return len(string) == 9 and intRangeCheck(string, 0, 999999999)


with open('AdventOfCode20/Day4/inputDay4.txt') as f:
    inputString = f.read()

print("Solution part one: ", partOne(inputString),
      "\nSolution part two: ", partTwo(inputString))
