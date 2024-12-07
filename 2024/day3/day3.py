from utils import read_input
import re


input = read_input("2024/day3")

MUL_PATTERN = "\\((\\d+),(\\d+)\\)"
INSTRUCTION_PATTERN_1 = "mul\\(\\d{1,3},\\d{1,3}\\)"
INSTRUCTION_PATTERN_2 = "(mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don\'t\\(\\))"

def apply_mul_instruction(instruction):
    a, b = map(int, MUL_PATTERN.search(instruction).groups())
    return a * b

def count_total_pt1(input):
    instructions = re.findall(INSTRUCTION_PATTERN_1, input)
    return sum(apply_mul_instruction(i) for i in instructions)

def count_total_pt2(input):
    instructions = re.findall(INSTRUCTION_PATTERN_2, input)
    total = 0
    do = True
    for i in instructions:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False

        elif do and i.startswith("mul"):
            total += apply_mul_instruction(i)
    return total

print("Total sum 1: ", count_total_pt1(input))
print("Total sum 2: ", count_total_pt2(input))