def hash(s):
    v = 0
    
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256

    return v

boxes = [[] for _ in range(256)]
focal_lengths = {}

file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 15/d15.txt"

with open(file_path, "r") as file:
    for instruction in file.readline().strip().split(","):
        if "-" in instruction:
            label = instruction[:-1]
            index = hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = instruction.split("=")
            length = int(length)
            
            index = hash(label)
            if label not in boxes[index]:
                boxes[index].append(label)
                
            focal_lengths[label] = length

total = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(total)
