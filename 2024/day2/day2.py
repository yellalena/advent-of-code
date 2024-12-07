from typing import Counter
from utils import read_input


input_lines = read_input("2024/day2")

reports = [list(map(int, report.split(" "))) for report in input_lines.split("\n")]

def is_ascending(value1, value2):
    return value1 < value2

def is_incorrect_order(report_direction, value1, value2):
    return (report_direction and not is_ascending(value1, value2)) or (not report_direction and is_ascending(value1, value2))

def verify_safety(report):
    ascending = is_ascending(report[0], report[1]) 
    j = 1
    for i in range(len(report)-1):
        if is_incorrect_order(ascending, report[i], report[j]):
            return False
        if abs(report[j] - report[i]) > 3 or abs(report[j] - report[i]) == 0:
            return False
        j+=1
    return True


def verify_safety_problem_dampener(report, error_count = 0):
    if len(report) < 3:
        return True
    if verify_safety(report):
        return True
    if error_count != 0:
        return False

    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if verify_safety_problem_dampener(new_report, error_count + 1):
            return True

    return False 


result = Counter(map(verify_safety, reports))
result2 = sum(map(verify_safety_problem_dampener, reports))

print("Safe reports: ", result[True])
print("Safe reports with problem dampener: ", result2)