import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()
input = [int(i) for i in input]

PREAMBLE_LENGTH = 25
idx = 0

while True:
    if idx >= len(input):
        print("Nothing found.")
        exit()
    chunk = input[idx:idx + PREAMBLE_LENGTH]
    target = input[idx+PREAMBLE_LENGTH]

    isValid = False
    for outerNum in chunk:
        for innerNum in chunk:
            if outerNum == innerNum:
                continue
            if innerNum + outerNum == target:
                isValid = True
                break
        if isValid:
            break
    if not isValid:
        print(f"Wrong: {target}")
        break
    idx += 1
