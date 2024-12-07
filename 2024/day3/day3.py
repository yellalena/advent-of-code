from utils import read_input
import re


input = read_input("2024/day3")

def apply_mul_instruction(instruction):
    a, b = re.findall("\\((\\d+),(\\d+)\\)", instruction)[0]
    return int(a) * int(b)

def count_total_pt1(input):
    result = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", input)
    total = 0
    for i in result:
        total += apply_mul_instruction(i)
    return total

def count_total_pt2(input):
    result = re.findall("(mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don\'t\\(\\))", input)
    total = 0
    do = True
    for i in result:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False

        if do and i.startswith("mul"):
            total += apply_mul_instruction(i)
    return total

print("Total sum 1: ", count_total_pt1(input))
print("Total sum 2: ", count_total_pt2(input))