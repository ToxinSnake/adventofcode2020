import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.read().split("\n\n")

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
totalValid = 0

for line in input:
    isValid = True
    for field in required:
        if re.search(f"{field}:",line) is None:
            isValid = False
            break
    if isValid:
        totalValid += 1

print(f"Valid: {totalValid}")
