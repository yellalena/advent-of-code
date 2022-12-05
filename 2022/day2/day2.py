with open("day2_input.txt", "r") as file:
    strategy_input = file.readlines()

test_input = ["A Y", "B X", "C Z"]

strategy_guide = [line.rstrip().split(" ") for line in strategy_input]

def get_total_score(strategy_guide: list):
    choice_scores_map = {"A": 1, "B": 2, "C": 3,
                     "X": 1, "Y": 2, "Z": 3}
    result_scores_map = {1: 0, 0: 3, 2: 6}

    total_score = 0
    for game_round in strategy_guide:
        winner = (3 + choice_scores_map[game_round[0]] - choice_scores_map[game_round[1]]) % 3
        total_score += choice_scores_map[game_round[1]] + result_scores_map[winner]
    return total_score

print(get_total_score(strategy_guide))
