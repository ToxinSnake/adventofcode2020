import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

RIGHT_COEFFICIENT = 3
DOWN_COEFFICIENT = 1

inputLenght = len(input)
modulus = len(input[0]) - 1
trees = 0
right = 0

for i in range(0,inputLenght-1):
    if(i == inputLenght):
        break
    right = (right + RIGHT_COEFFICIENT) % modulus
    isTree = input[i+DOWN_COEFFICIENT][right] == '#'
    if(isTree):
        trees += 1

print(f"Trees: {trees}")