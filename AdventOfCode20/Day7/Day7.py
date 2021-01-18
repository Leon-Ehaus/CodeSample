import networkx as nx
import matplotlib.pyplot as plt


def partOne(inputStringArr) -> int:
    ruleGraph = determineWeightedGraph(inputStringArr)

    reachableNodes = nx.ancestors(ruleGraph, "shiny gold bag")
    return len(reachableNodes)


def isollate(lineString) -> list:
    """splis the lineString into an array with the bag number and types"""
    lineString = lineString.replace("bags", "bag")
    lineString = lineString.replace(".", "")
    lineStringArr = lineString.split("contain")
    root = lineStringArr[0].strip()
    if lineStringArr[1] == " no other bag":
        return [root]
    lineStringArr = [x.strip() for x in lineStringArr[1].split(",")]
    leafList = []
    for x in lineStringArr:
        leafList = leafList + [x[0]]+[x[2:]]

    return [root] + leafList


def partTwo(inputStringArr) -> int:
    ruleGraph = determineWeightedGraph(inputStringArr)
    weight = determineTotalWeight(ruleGraph, "shiny gold bag")

    return weight


def determineTotalWeight(graph, node) -> int:
    """determines the weight of the node (how many bags are included in one)"""
    neighbors = nx.neighbors(graph, node)
    weight = 0
    for x in neighbors:
        localweight = int(graph[node][x]["weight"])
        weight += localweight * determineTotalWeight(graph, x) + localweight

    return weight


def determineWeightedGraph(inputStringArr):
    """creates a weighted directed graph representing the rules from inputStringArr"""
    ruleGraph = nx.DiGraph()

    for line in inputStringArr:
        rule = isollate(line)
        for weight, edge in zip(rule[1::2], rule[2::2]):
            ruleGraph.add_edge(rule[0], edge, weight=int(weight))

    return ruleGraph


with open('AdventOfCode20/Day7/inputDay7.txt') as f:
    inputArr = f.readlines()

inputArr = [x.strip() for x in inputArr]


print("Solution part one: ", partOne(inputArr),
      "\nSolution part two: ", partTwo(inputArr))
