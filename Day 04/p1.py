t = 0
file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 04/d4.txt"

with open(file_path , 'r') as file:
    for x in file:
        x = x.split(":")[1].strip()
        a, b = [list(map(int, k.split())) for k in x.split(" | ")]
        j = sum(q in a for q in b)
        if j > 0:
            t += 2 ** (j - 1)

print(t)