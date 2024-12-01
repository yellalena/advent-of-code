
from typing import Counter
from utils import read_input


input_lines = read_input("2024/day1")

list1, list2 = map(list, zip(*(map(int, line.split("   ")) for line in input_lines.split("\n"))))

list1.sort()
list2.sort()

total_distance = 0

for pair in zip(list1, list2):
    total_distance += abs(pair[1] - pair[0])

print(total_distance)

# ======== part 2 =========

total_similarity_score = 0

list2_counter = Counter(list2)
for item in list1:
    total_similarity_score += item * list2_counter[item]

print(total_similarity_score)