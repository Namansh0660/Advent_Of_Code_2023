m = {}
file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 04/d4.txt"

with open(file_path , 'r') as file:
    for i, x in enumerate(file):
        if i not in m:
            m[i] = 1

        x = x.split(":")[1].strip()
        a, b = [list(map(int, k.split())) for k in x.split(" | ")]
        j = sum(q in a for q in b)
        
        for n in range(i + 1, i + j + 1):
            m[n] = m.get(n, 1) + m[i]

print(sum(m.values()))