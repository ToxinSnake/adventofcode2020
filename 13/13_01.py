import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
MY_DEPARTURE = int(file.readline())
input = file.readline().split(",")
input = [int(x) for x in input if x != "x"]

departure = 0
busid = 0
for bus in input:
    nextDep = 0
    while nextDep < MY_DEPARTURE:
        nextDep += bus
    if nextDep < departure or departure == 0:
        departure = nextDep
        busid = bus

print(f"Wait (min): {departure - MY_DEPARTURE}")
print(f"Solution: {(departure - MY_DEPARTURE) * busid}")
