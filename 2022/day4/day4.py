with open("day4_input.txt") as file:
    pairs = [line.split(",") for line in file.readlines()]

# part 1 

count_fully_contained = 0
for pair in pairs:
    elf_one = [int(i) for i in pair[0].split("-")]
    elf_two = [int(i) for i in pair[1].split("-")]
    if (elf_one[0] <= elf_two[0] and elf_one[1] >= elf_two[1]) or \
        (elf_two[0] <= elf_one[0] and elf_two[1] >= elf_one[1]):
            count_fully_contained += 1

print(count_fully_contained)

# part 2

count_overlapping = 0
for pair in pairs:
    elf_one = [int(i) for i in pair[0].split("-")]
    elf_two = [int(i) for i in pair[1].split("-")]
    if max(elf_one[0],elf_two[0]) <= min(elf_one[1], elf_two[1]):
            count_overlapping += 1

print(count_overlapping)