'''
Q: "Why are we using "o1e", "t2o", "t3e", etc.?

A: Take the example of "eighthree7":
    As "three" is replaced first, if we directly replace it with "3" 
    then the string becomes "eigh37" which will give 37, ignoring the original
    "eight" and thus producing the incorrect result.
    
    However, if we replace "three" with "t3e" the string becomes "eight3e7"
    which still allows the "eight" to be changed into a digit. The will then 
    become "e8t3e7" which will give "87" correctly.
'''

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
