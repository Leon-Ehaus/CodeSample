def partOne(inputMap)-> int:
    mapsize = len(inputMap[0])
    treeCount = 0
    for i, x in enumerate(inputMap):
        if "#" == x[(i*3) % mapsize]:
            treeCount += 1
    return treeCount





with open('AdventOfCode20/input.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]
print(partOne(inputArr))