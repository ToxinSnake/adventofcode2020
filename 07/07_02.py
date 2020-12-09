import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

mybag = "shiny gold"
rColorRule = r"^(\S*\s\S*)(?=\s)"
rContainColors = r"(?<=\d\s)\S*\s\S*"
rContainQuantity = r"\d{1,}"

def get_bag_count(bag: str) -> int:
    mybagMustContain = set()
    total = 0
    
    for line in input:
        current = re.findall(rColorRule, line)[0]
        if current == bag:
            colors = re.findall(rContainColors, line)
            quantity = re.findall(rContainQuantity, line)
            for c, q in zip(colors, quantity):
                mybagMustContain.add((c,int(q)))
            break

    for color in mybagMustContain:
        total += color[1] + color[1] * get_bag_count(color[0])
    return total

if __name__ == "__main__":
    sum = get_bag_count(mybag)
    print(f"Total Bags: {sum}")
    