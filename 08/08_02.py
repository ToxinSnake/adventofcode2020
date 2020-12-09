import os

def switch(idx: int, text: list) -> list:
    opcode = text[idx][:3]
    if opcode == "nop":
        text[idx] = text[idx].replace("nop", "jmp")
    elif opcode == "jmp":
        text[idx] = text[idx].replace("jmp", "nop")
    return text

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()
jmpnopIdx = []
terminated = False

for idx, line in enumerate(input):
    opcode = line[:3]
    if opcode == "nop" or opcode == "jmp":
        jmpnopIdx.append(idx)

for op in jmpnopIdx:
    code = switch(op, input.copy())
    
    visited = []
    accumulator = 0
    idx = 0

    while True:
        if idx >= len(code):
            terminated = True
            break

        if idx in visited:
            break

        visited.append(idx)
        line = code[idx].rstrip()
        opcode = line[:3]

        if opcode == "acc":
            accumulator += int(line[4:])
        elif opcode == "jmp":
            idx += int(line[4:])
            continue
        idx += 1

    if terminated:
        break

print(f"acc: {accumulator}")
