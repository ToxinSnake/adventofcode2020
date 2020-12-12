import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()
input = [int(i) for i in input]

WEAK_NUMBER = 258585477
outerIdx = 0
innerIdx = 1

while outerIdx <= len(input):
    innerIdx = outerIdx + 1
    while innerIdx <= len(input):
        chunk = input[outerIdx:innerIdx]
        if sum(chunk) == WEAK_NUMBER:
            solution = min(chunk) + max(chunk)
            print(f"Solution: {solution}")
            exit()
        innerIdx += 1
    outerIdx += 1
    