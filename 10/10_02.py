import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/exmpsmall.txt", "r")
input = file.readlines()
input = [int(i) for i in input]
input.sort()

BIGGEST_ADAPTER = max(input)

idx = [1] + [0] * BIGGEST_ADAPTER + [0,0]
for line in input:
    idx[line] = idx[line-1] + idx[line-2] + idx[line-3]
    if line == BIGGEST_ADAPTER:
        print(f"{idx[line]}") 
