import os

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
numbers = file.readlines()

for num in numbers:
    for inner1 in numbers:
        for inner2 in numbers:
            if(int(num)+int(inner1)+int(inner2) == 2020):
                print(f"{int(num)} + {int(inner1)} + {int(inner2)} = {int(num)+int(inner1)+int(inner2)}")
                print(f"{int(num)} * {int(inner1)} * {int(inner2)} = {int(num)*int(inner1)*int(inner2)}")
                exit()