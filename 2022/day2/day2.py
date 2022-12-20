with open("day2_input.txt", "r") as file:
    strategy_guide = [line.rstrip().split(" ") for line in file.readlines()]

test_strategy_guide = [line.rstrip().split(" ") for line in ["A Y", "B X", "C Z"]]

choice_scores_map = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
result_scores_map = {1: 0, 0: 3, 2: 6}

def get_total_score_v1(strategy_guide: list):
    total_score = 0
    for elf, me in strategy_guide:
        winner = (3 + choice_scores_map[elf] - choice_scores_map[me]) % 3
        total_score += choice_scores_map[me] + result_scores_map[winner]
    return total_score

print(get_total_score_v1(strategy_guide))

result_scores_map= {"X": 0, "Y": 3, "Z": 6}

def get_total_score_v2(strategy_guide: list):
    total_score = 0
    for elf, me in strategy_guide:
        choice = (choice_scores_map[elf] + (choice_scores_map[me] - 2) + 2) % 3
        total_score += choice + result_scores_map[me] + 1
    return total_score

print(get_total_score_v2(strategy_guide))
