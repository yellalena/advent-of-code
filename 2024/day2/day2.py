from typing import Counter
from utils import read_input


input_lines = read_input("2024/day2")
reports = [list(map(int, report.split(" "))) for report in input_lines.split("\n")]

def is_ascending(value1, value2):
    return value1 < value2

def verify_safety(report):
    ascending = is_ascending(report[0], report[1]) 
    j = 1
    for i in range(len(report)-1):
        if not (ascending and is_ascending(report[i], report[j])) and not (not ascending and not is_ascending(report[i], report[j])):
            return False
        if abs(report[j] - report[i]) > 3 or abs(report[j] - report[i]) == 0:
            return False
        j+=1
    return True

result = Counter(map(verify_safety, reports))

print("Safe reports: ", result[True])