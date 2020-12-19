import os
import re
import math

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()
rMEM_OFFSET = r"\d*(?=\])"
rMEM_VALUE = r"(?<=\=\s)\d*"
mem = dict()

def decode(mask: str, address: str) -> list:
    for idx, char in enumerate(mask):
        if char == "0":
            continue
        address = address[:idx] + char + address[idx + 1:]

    matches = re.finditer("X", address)
    matches = [match.start() for match in matches]
    address_space = []

    for i in range(0, int(math.pow(2, len(matches)))):
        current = f"{i:b}".zfill(len(matches))
        temp = address
        for idx, char in enumerate(current):
            temp = temp[:matches[idx]] + char + temp[matches[idx] + 1:]
        address_space.append(int("0b"+temp,2))
    return address_space

for line in input:
    if "mask" in line:
        mask = line.split("= ")[1].rstrip("\n")
        continue


    offset = int(re.findall(rMEM_OFFSET, line)[0])
    value = int(re.findall(rMEM_VALUE, line)[0])

    address_space = decode(mask, f"{offset:b}".zfill(36))

    for a in address_space:
        mem[a] = value

print(f"Sum: {sum(mem.values())}")