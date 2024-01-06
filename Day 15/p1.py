
def hash(s):
    v = 0
    
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256

    return v

file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 15/d15.txt"

with open(file_path, "r") as file:
    input_data = file.readline().strip()

result = sum(map(hash, input_data.split(",")))
print(result)
