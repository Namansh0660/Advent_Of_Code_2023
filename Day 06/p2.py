file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 06/d6.txt"

with open(file_path , 'r') as file:
    times, distances = [list(map(int, ["".join(line.split(":")[1].split())])) for line in file]

n = 1

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1
    n *= margin

print(n)