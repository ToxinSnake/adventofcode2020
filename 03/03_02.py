import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
#file = open(f"{os.path.dirname(os.path.abspath(__file__))}/example.txt", "r")
input = file.readlines()

RIGHT_COEFFICIENTS = [1,3,5,7,1]
DOWN_COEFFICIENTS = [1,1,1,1,2]

inputLenght = len(input)
modulus = len(input[0]) - 1
totalTrees = []

for r, d in zip(RIGHT_COEFFICIENTS, DOWN_COEFFICIENTS):
    trees = 0
    right = 0
    for i in range(0,inputLenght,d):
        if(i + d > inputLenght-1):
            totalTrees.append(trees)
            break
        right = (right + r) % modulus
        isTree = input[i+d][right] == '#'
        if(isTree):
            trees += 1

result = 1
for i in totalTrees:
    result = result * i
print(f"Trees: {totalTrees}")
print(f"Result: {result}")