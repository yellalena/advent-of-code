from utils import read_input


input = read_input("2024/day4", readlines=True)

input_matrix = [list(line.strip()) for line in input]

directions = [
            (0, 1),  # right
            (0, -1), # left
            (1, 0),  # down
            (-1, 0), # up
            (1, 1),  # diagonal down-right
            (-1, -1),# diagonal up-left
            (1, -1), # diagonal down-left
            (-1, 1)  # diagonal up-right
        ]

def is_valid(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def check_direction(x, y, dx, dy, word, matrix):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny, matrix) or matrix[nx][ny] != word[i]:
            return False
    return True

def count_words(matrix):
    word = "XMAS"
    xmas_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == word[0]:
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy, word, matrix):
                        xmas_count += 1
    return xmas_count

total = count_words(input_matrix)
print("Total XMASes: ", total)
