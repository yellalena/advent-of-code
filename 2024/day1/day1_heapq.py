
from heapq import heappop, heappush
from typing import Counter
from utils import read_input


input_lines = read_input("2024/day1")

list1 = []
list2 = []
for line in input_lines.split("\n"):
    a, b = map(int, line.split("   "))
    heappush(list1, a)
    heappush(list2, b)

list2_counter = Counter(list2)

total_distance = 0
total_similarity_score = 0

while (list1 and list2):
    a = heappop(list1)
    b = heappop(list2)
    total_distance += abs(a - b)
    total_similarity_score += a * list2_counter[a]

print("Total distance: ", total_distance)
print("Total similarity score: ", total_similarity_score)