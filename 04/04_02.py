import os
import re

file = open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt", "r")
input = file.read().split("\n\n")

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
checks = {
    "byr": (r"(?<=byr:)\d{4}\b", 1920, 2002),
    "iyr": (r"(?<=iyr:)\d{4}\b", 2010, 2020),
    "eyr": (r"(?<=eyr:)\d{4}\b", 2020, 2030),
    "hgt": r"(cm|in)",
    "hgtcm": (r"(?<=hgt:)\d*(?=cm)", 150,193),
    "hgtin": (r"(?<=hgt:)\d*(?=in)", 59,76),
    "hcl": r"(?<=hcl:#)[0-9a-f]{6}\b",
    "ecl": (r"(?<=ecl:)\S*", ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": r"pid:\d{9}\b"
}

totalValid = 0

for line in input:
    isValid = True
    for field in required:
        
        if field == "byr" or field == "iyr" or field == "eyr":
            num = re.search(checks[field][0], line)
            if num:
                num = int(num.group())
                if checks[field][1] > num or num > checks[field][2]:
                    isValid = False
                    break
            else:
                isValid = False
                break
        
        elif field == "hgt":
            meas = re.search(checks[field], line)
            if meas:
                meas = meas.group()
                hgt = re.search(checks[f"{field}{meas}"][0], line)
                if hgt:
                    hgt = int(hgt.group())
                    if checks[f"{field}{meas}"][1] > hgt or hgt > checks[f"{field}{meas}"][2]:
                        isValid = False
                        break
                else:
                    isValid = False
                    break
            else:
                isValid = False
                break

        elif field == "hcl":
            hcl = re.search(checks[field], line)
            if hcl is None:
                isValid = False
                break

        elif field == "ecl":
            ecl = re.search(checks[field][0], line)
            if ecl:
                ecl = ecl.group()
                if ecl not in checks[field][1]:
                    isValid = False
                    break
            else:
                isValid = False
                break

        elif field == "pid":
            pid = re.search(checks[field], line)
            if pid is None:
                isValid = False
                break

    if isValid:
        totalValid += 1

print(f"Valid: {totalValid}")