file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 14/d14.txt"
with open(file_path , 'r')as file:
    grid = file.read().splitlines()
grid = list(map("".join, zip(*grid)))
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
grid = list(map("".join, zip(*grid)))

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))