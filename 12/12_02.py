import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

CARDINALS = ["S", "W", "N", "E"]
ship_position = [
    0, #S
    0, #W
    0, #N
    0  #E
]
waypoint_position = [
    0, #S
    0, #W
    1, #N
    10  #E
]

for line in input:
    cmd = line[0]
    arg = int(line[1:])

    if cmd in CARDINALS:
        waypoint_position[CARDINALS.index(cmd)] += arg
    elif cmd in "LR":
        copy = waypoint_position.copy()
        if cmd == "L":
            shift_amount = -int(arg / 90)
        else:
            shift_amount = int(arg / 90)
        for i in range(0, 4):
            dest = (i + shift_amount) % 4
            waypoint_position[dest] = copy[i] 

    elif cmd == "F":
        for times in range(0, arg):
            for i, n in enumerate(ship_position):
                ship_position[i] += waypoint_position[i]

test = 1

eastWest = abs(ship_position[1] - ship_position[3])
northSouth = abs(ship_position[2] - ship_position[0])
print(f"Manhatten distance: {eastWest + northSouth}")
