import re

def convert_to_numeric(line):
    replacements = {
        "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", 
        "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"
    }
    for word, number in replacements.items():
        line = re.sub(word, number, line)
    return line

total = 0
with open("day_1.txt", "r") as file:
    for line in file:
        line = convert_to_numeric(line)
        line = re.sub("[a-z]", "", line.strip())
        merged = int(line[0] + line[-1])
        total += merged

print(total)
