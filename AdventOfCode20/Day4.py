def partOne(inputString):

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


def keyCheck(x):
    return{
        'byr': intRangeCheck(x[1], 1920, 2002),
        'iyr': intRangeCheck(x[1], 2010, 2020),
        'eyr': intRangeCheck(x[1], 2020, 2030),
        'hgt': hgt(x[1]),
        'hcl': hcl(x[1]),
        'ecl': ecl(x[1]),
        'pid': pid(x[1]),
        'cid': True
    }.get(x[0], False)


def intRangeCheck(string, minVal, maxVal):
    try:
        return(minVal <= int(string) <= maxVal)
    except ValueError:
        return False


def hgt(string):
    stringEnd = string[-2:]
    if stringEnd == "cm":
        return intRangeCheck(string[:-2], 150, 193)
    elif stringEnd == "in":
        return intRangeCheck(string[:-2], 59, 76)
    else:
        return False


def hcl(string):
    if string[0] == '#':
        try:
            int(string[1:], 16)
            return True
        except ValueError:
            return False
    return False


def ecl(string):
    return string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid(string):
    return len(string) == 9 and intRangeCheck(string, 0, 999999999)


with open('AdventOfCode20/input.txt') as f:
    inputString = f.read()

print("Solution part one: ", partOne(inputString),
      "\nSolution part two: ", partTwo(inputString))
