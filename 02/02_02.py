import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

valid = 0

for line in input:
    index1 = int(re.findall(r"^\d*", line)[0])
    index2 = int(re.findall(r"(?<=-)\d*", line)[0])
    char = re.findall(r"(?<=\s)\D(?=:)", line)[0]
    passwd = line.split(" ")[2].rstrip()

    index1_contains = passwd[index1-1] == char
    index2_contains = passwd[index2-1] == char

    if((index1_contains == True and index2_contains == False) or (index1_contains == False and index2_contains == True)):
        valid += 1
    
print(f"Valid passwords: {valid}")