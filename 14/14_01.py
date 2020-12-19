import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()
rMEM_OFFSET = r"\d*(?=\])"
rMEM_VALUE = r"(?<=\=\s)\d*"
mem = dict()

for line in input:
    if "mask" in line:
        mask = line.split("= ")[1].rstrip("\n")
        continue

    offset = int(re.findall(rMEM_OFFSET, line)[0])
    value = int(re.findall(rMEM_VALUE, line)[0])

    #or to set 1
    oneMask = int("0b" + mask.replace("X", "0"), 2)
    result = value | oneMask

    #and to set 0
    zeroMask = int("0b" + mask.replace("X", "1"), 2)
    result = result & zeroMask

    mem[offset] = result

print(f"Sum: {sum(mem.values())}")