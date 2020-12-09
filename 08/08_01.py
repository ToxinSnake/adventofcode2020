import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

visited = set()
lastIdx = 0
accumulator = 0
idx = 0

while True:
    if idx in visited:
        break
    visited.add(idx)
    line = input[idx].rstrip()
    opcode = line[:3]

    if opcode == "nop":
        idx += 1
        continue
    elif opcode == "acc":
        accumulator += int(line[4:])
        idx += 1
        continue
    elif opcode == "jmp":
        idx += int(line[4:])
        continue

print(f"acc: {accumulator}")
