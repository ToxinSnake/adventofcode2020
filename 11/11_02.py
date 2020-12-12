import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
lastiter = file.readlines()
currentiter = lastiter.copy()

LINE_LENGTH = len(lastiter[0]) - 2
LAST_INDEX = len(lastiter) - 1
EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"

def find_left_right(isLeft: bool, i: int, j: int) -> str:
    if isLeft:
        while j >= 0:
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            j -= 1
    else:
        while j <= LINE_LENGTH:
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            j += 1
    return FLOOR

def find_up_down(isUp: bool, i: int, j: int) -> str:
    if isUp:        
        while i >= 0: 
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            i -= 1
    else:
        while i <= LAST_INDEX: 
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            i += 1
    return FLOOR

def find_diagonal(mode: int, i: int, j: int) -> str:
    #diagonal up left
    if mode == 0:
        while i >= 0 and j >= 0:
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            i -= 1
            j -= 1
        return FLOOR
    #diagonal up right
    if mode == 1:
        while i >= 0 and j <= LINE_LENGTH:
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            i -= 1
            j += 1
        return FLOOR
    #diagonal down left
    if mode == 2:
        while i <= LAST_INDEX and j >= 0:
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            i += 1
            j -= 1
        return FLOOR
    #diagonal down right
    if mode == 3:
        while i <= LAST_INDEX and j <= LINE_LENGTH:
            if lastiter[i][j] == OCCUPIED or lastiter[i][j] == EMPTY:
                return lastiter[i][j]
            i += 1
            j += 1
        return FLOOR

while True:
    lastiter = currentiter.copy()
    for i, line in enumerate(lastiter):
        line = line.replace("\n", "")
        for j, char in enumerate(line):
            if char == FLOOR:
                continue           
            adjacent = []

            #left
            adjacent.append(find_left_right(True, i, j-1))
            #right
            adjacent.append(find_left_right(False, i, j+1))
            #up
            adjacent.append(find_up_down(True, i-1, j))
            #down
            adjacent.append(find_up_down(False, i+1, j))            
            #diagonal up left
            adjacent.append(find_diagonal(0, i-1, j-1))
            #diagonal up right
            adjacent.append(find_diagonal(1, i-1, j+1))
            #diagonal down left
            adjacent.append(find_diagonal(2, i+1, j-1))
            #diagonal down right
            adjacent.append(find_diagonal(3, i+1, j+1))
           
            if char == EMPTY:            
                if OCCUPIED not in adjacent:
                    currentiter[i] = currentiter[i][:j] + OCCUPIED + currentiter[i][j+1:]
            if char == OCCUPIED:
                if adjacent.count(OCCUPIED) > 4:
                    currentiter[i] = currentiter[i][:j] + EMPTY + currentiter[i][j+1:]
    if currentiter == lastiter:
        occs = 0
        for line in currentiter:
            occs += line.count(OCCUPIED)
        print(f"Occupied Seats: {occs}")
        break  
