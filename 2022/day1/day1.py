with open("day1_input.txt", "r") as file:
    input_lines = file.read()

processed_input = [batch.split("\n") for batch in input_lines.split("\n\n")]

def get_max_sum_of_calories(list_of_elves: list, n_top_of_elves: int):
    sums_list = [
        sum([int(i) for i in batch]) for batch in list_of_elves 
    ]
    sums_list.sort(reverse=True)
    return sum(sums_list[:n_top_of_elves])

print(get_max_sum_of_calories(processed_input, 1)) 
print(get_max_sum_of_calories(processed_input, 3)) 
    