import string
from turtle import back

with open("day3_input.txt", "r") as file:
    backpacks = file.readlines()

priorities = {m: n for n, m in enumerate(string.ascii_letters, 1)}

def get_total_score_v1(backpacks):
    total_score = 0
    for backpack in backpacks:
        middle = int(len(backpack)/2)
        pt1 = backpack[:middle]
        pt2 = dict.fromkeys(backpack[middle:])
        for item1 in pt1:
            if item1 in pt2:
                total_score += priorities[item1]
                break
    return total_score

print(get_total_score_v1(backpacks))

def get_total_score_v2(backpacks):
    def elf_groups():
        for i in range(0, len(backpacks), 3):
            yield backpacks[i:i+3]

    total_score = 0
    for elf1, elf2, elf3 in elf_groups():
        elf2 = dict.fromkeys(elf2)
        elf3 = dict.fromkeys(elf3)
        for item in elf1:
            if item in elf2 and item in elf3:
                total_score += priorities[item]
                break
    return total_score

print(get_total_score_v2(backpacks))