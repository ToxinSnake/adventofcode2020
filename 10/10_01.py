import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()
input = [int(i) for i in input]
input.sort()

BIGGEST_ADAPTER = max(input)
MY_ADAPTER = BIGGEST_ADAPTER + 3
oneDiff = 0
threeDiff = 0

lastAdapter = 0

while lastAdapter != BIGGEST_ADAPTER:
    currentAdapter = min(input)
    diff = currentAdapter - lastAdapter
    if diff == 1:
        oneDiff += 1
    elif diff == 3:
        threeDiff += 1
    lastAdapter = currentAdapter
    input.remove(min(input))

#My adapter last, always three difference
threeDiff += 1

print(f"One difference: {oneDiff}\nThree difference: {threeDiff}\nResult: {oneDiff * threeDiff}")