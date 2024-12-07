from utils import read_input
import re


input = read_input("2024/day3")

result = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", input)

def apply_mul_instruction(instruction):
    a, b = re.findall("\\((\\d+),(\\d+)\\)", instruction)[0]
    return int(a) * int(b)

total = 0
for i in result:
    total += apply_mul_instruction(i)

print("Total sum: ", total)