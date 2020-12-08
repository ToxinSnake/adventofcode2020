import os
from functools import reduce

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.read().split("\n\n")

totalyes = 0

for line in input:
    allyes = None
    for answer in line.split("\n"):
        yes = [char for char in answer]
        if allyes is None:
            allyes = yes
            continue
        allyes = [a for a in yes if a in allyes]
    totalyes += len(allyes)
    
print(f"Yes:{totalyes}")