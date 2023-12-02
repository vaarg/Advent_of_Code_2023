import re

total = 0
with (open('day_1.txt') as file):
    for line in file:
        line = re.sub("[a-z]", "", line.strip())
        merged = int(line[0] + line[-1])
        total += merged
        
print(total)
