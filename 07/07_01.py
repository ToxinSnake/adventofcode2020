import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.readlines()

mybag = "shiny gold"
rColorRule = r"^(\S*\s\S*)(?=\s)"
rContainColors = r"(?<=\d\s)\S*\s\S*"
rContainQuantity = r"\d{1,}"

def contain_recurse(bag: str) -> str:
    result = set()
    for line in input:
        supported = re.findall(rContainColors, line)
        if bag in supported:
            current = re.findall(rColorRule, line)[0]
            result.add(current)    
    for color in result:
        result = result.union(contain_recurse(color))        
    return result

if __name__ == "__main__":
    canContain = set()

    for line in input:
        current = re.findall(rColorRule, line)[0]
        can_contain = re.findall(rContainColors, line)
        can_contain_mybag = len([c for c in can_contain if c == mybag]) > 0
        if can_contain_mybag:
            canContain.add(current)
            
    print(f"Direct: {canContain}")

    for t in canContain:
        canContain = canContain.union(contain_recurse(t))

    print(f"Can Contain: {len(canContain)}")
