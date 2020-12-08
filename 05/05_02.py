import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

highestId = 0
lowestId = 9999
ids = []

for line in input:
    row = line.replace("F", "0")
    row = row.replace("B", "1")
    row = f"0b{row[:7]}"
    row = int(row, 2)

    col = line.replace("L", "0")
    col = col.replace("R", "1")
    col = f"0b{col[7:]}"
    col = int(col, 2)

    id = row * 8 + col
    ids.append(id)

    if id > highestId:
        highestId = id
    if id < lowestId:
        lowestId = id

ids.sort()
missing = [x for x in range(lowestId, highestId) if x not in ids]
print(f"Missing: {missing}")