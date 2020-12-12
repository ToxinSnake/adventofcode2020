import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
lastiter = file.readlines()
currentiter = lastiter.copy()

LAST_INDEX = len(lastiter) - 1
EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"

while True:
    lastiter = currentiter.copy()
    for i, line in enumerate(lastiter):
        line = line.replace("\n", "")
        for j, char in enumerate(line):
            above = None
            below = None
            if i != 0:
                above = lastiter[i-1]
            if i != LAST_INDEX:
                below = lastiter[i+1]

            if char == FLOOR:
                continue
            
            adjacent = []
            if j != 0:
                adjacent.append(line[j-1])
            if j != len(line) - 1:
                adjacent.append(line[j+1])

            if above is not None: #is not the top most row
                adjacent.append(above[j])
                if j != 0: #is not the left most char
                    adjacent.append(above[j-1])
                if j != len(line) - 1: #is not the right most char
                    adjacent.append(above[j+1])
            if below is not None: #is not the bottom most row
                adjacent.append(below[j])
                if j != 0: #is not the left most char
                    adjacent.append(below[j-1])
                if j != len(line) - 1: #is not the right most char
                    adjacent.append(below[j+1])
            
            if char == EMPTY:            
                if OCCUPIED not in adjacent:
                    currentiter[i] = currentiter[i][:j] + OCCUPIED + currentiter[i][j+1:]
            if char == OCCUPIED:
                if adjacent.count(OCCUPIED) > 3:
                    currentiter[i] = currentiter[i][:j] + EMPTY + currentiter[i][j+1:]
    if currentiter == lastiter:
        occs = 0
        for line in currentiter:
            occs += line.count(OCCUPIED)
        print(f"Occupied Seats: {occs}")
        break  
