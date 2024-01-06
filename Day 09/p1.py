def extrapolate(array):
    if all(x == 0 for x in array):
        return 0

    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    return array[-1] + diff

total = 0

file_path = "C:/Users/Hp/Documents/Visual Studio/AOC_2023/Day 09/d9.txt"

with open(file_path , 'r') as file:
    for line in file:
        nums = list(map(int, line.split()))
        total += extrapolate(nums)

print(total)