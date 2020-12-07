import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

valid = 0

for line in input:
    min = int(re.findall(r"^\d*", line)[0])
    max = int(re.findall(r"(?<=-)\d*", line)[0])
    char = re.findall(r"(?<=\s)\D(?=:)", line)[0]
    passwd = line.split(" ")[2].rstrip()

    count = passwd.count(char)

    if(min <= count <= max):
        valid += 1

print(f"Valid passwords: {valid}")