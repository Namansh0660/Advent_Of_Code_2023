t = 0

file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 02/d2.txt"

with open(file_path , 'r') as file:
    for i, x in enumerate(file):
        gs = x.strip().split(": ")[1].split("; ")
        for g in gs:
            m = {"red": 0, "green": 0, "blue": 0}
            for e in g.split(", "):
                a, b = e.split()
                m[b] = int(a)
            if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
                break
        else:
            t += i + 1
print(t)