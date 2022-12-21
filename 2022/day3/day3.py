import string

with open("day3_input.txt", "r") as file:
    backpacks = file.readlines()

priorities = {m: n for n, m in enumerate(string.ascii_letters, 1)}

total_score = 0
for backpack in backpacks:
    middle = int(len(backpack)/2)
    pt1 = backpack[:middle]
    pt2 = dict.fromkeys(backpack[middle:])
    for item1 in pt1:
        if item1 in pt2:
            total_score += priorities[item1]
            break

print(total_score)