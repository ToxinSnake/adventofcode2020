import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

CARDINALS = ["S", "W", "N", "E"]
positions = {
    "S": 0,
    "W": 0,
    "N": 0,
    "E": 0
}
facing = "E"

for line in input:
    cmd = line[0]
    arg = int(line[1:])

    if cmd in CARDINALS:
        positions[cmd] += arg
    elif cmd == "R" or cmd == "L":
        idx = CARDINALS.index(facing)
        if cmd == "L":
            idx = int((idx - arg/90) % 4)
        else:
            idx = int((idx + arg/90) % 4)
        facing = CARDINALS[idx]
    elif cmd == "F":
        positions[facing] += arg

eastWest = abs(positions["W"] - positions["E"])
northSouth = abs(positions["N"] - positions["S"])
print(f"Manhatten distance: {eastWest + northSouth}")
