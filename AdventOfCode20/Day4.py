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




with open('AdventOfCode20/input.txt') as f:
    inputString = f.read()

print("Solution part one: ", partOne(inputString),
      "\nSolution part two: ", 0)
