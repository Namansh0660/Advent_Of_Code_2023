t = 0

file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 01/test.txt"

with open(file_path, 'r') as file:
    for x in file:
        digits = [ch for ch in x if ch.isdigit()]
        t += int(digits[0] + digits[-1])

print(t)