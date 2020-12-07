import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
numbers = file.readlines()

for num in numbers:
    for inner in numbers:
        if(int(num)+int(inner) == 2020):
            print(f"{int(num)} + {int(inner)} = {int(num)+int(inner)}")
            print(f"{int(num)} * {int(inner)} = {int(num)*int(inner)}")
            exit()