def is_line_possible(words):
    color_limits = {'red': 12, 'green': 13, 'blue': 14}

    for n in range(1, len(words)):
        for color, limit in color_limits.items():
            if color in words[n] and int(words[n-1]) > limit:
                return False
    return True

with (open('day_2.txt') as file):
    id_sum = 0
    for line in file:
        words = line.split()
        game_id = int(words[1].replace(":", ""))
        words = words[2:]
        if is_line_possible(words):
            id_sum += game_id
        
print(f"Final sum is {id_sum}")
