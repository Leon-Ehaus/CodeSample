import networkx as nx
import matplotlib.pyplot as plt


def partOne(inputStringArr) -> int:
    pos = 0
    accumulator = 0
    visitedPositions = [0]
    while True:
        output = runLine(inputStringArr[pos], accumulator, pos)
        accumulator = output[0]
        pos = output[1]
        if pos in visitedPositions:
            break
        else:
            visitedPositions.append(pos)

    return accumulator


def runLine(lineString, accumulator, pos) -> (int, int):
    """executes one line and returns new value of acc and new pos"""
    lineArr = lineString.split(" ")

    if lineArr[0] == "acc":
        accumulator = accumulator + int(lineArr[1])
    elif lineArr[0] == "jmp":
        return (accumulator, pos + int(lineArr[1]))

    return (accumulator, pos + 1)


def partTwo(inputStringArr) -> int:
    programGraph = createGraph(inputStringArr)

    # list of lines with wich the program terminates when reached
    endRange = nx.ancestors(programGraph, "end")
    # list of lines the program executes
    programScope = nx.descendants(programGraph, 0)

    # find and exchange the nessesary line operation
    attributes = nx.get_node_attributes(programGraph, "op")
    for key, value in attributes.items():
        if key in programScope:
            if value == "jmp":
                if key + 1 in endRange:
                    inputStringArr[key] = inputStringArr[key].replace(
                        "jmp", "nop")
            elif value == "nop":
                newLineNr = programGraph.nodes[key]["arg"] + key
                if newLineNr >= len(inputStringArr) or newLineNr in endRange:
                    inputStringArr[key] = inputStringArr[key].replace(
                        "nop", "jmp")

    # execute the changed program
    pos = 0
    accumulator = 0
    while pos < len(inputStringArr):
        output = runLine(inputStringArr[pos], accumulator, pos)
        accumulator = output[0]
        pos = output[1]

    return accumulator


def createGraph(inputStringArr):
    """returns a directed graph representing the order of execution"""
    programGraph = nx.DiGraph()
    for index, line in enumerate(inputStringArr):
        lineArr = line.split(" ")
        destination = index + 1
        if lineArr[0] == "jmp":
            destination = index + int(lineArr[1])
        if destination >= len(inputStringArr):
            destination = "end"

        programGraph.add_edge(index, destination)
        programGraph.nodes[index]["op"] = lineArr[0]
        programGraph.nodes[index]["arg"] = lineArr[1]

    return programGraph


with open('AdventOfCode20/Day8/inputDay8.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
