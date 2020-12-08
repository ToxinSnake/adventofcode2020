import os
from functools import reduce

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.read().split("\n\n")

num = map(lambda l: len("".join(set(l.replace("\n","")))), input)
num = reduce(lambda x,y: x+y, num)

print(f"Yes:{num}")