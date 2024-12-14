from utils import read_input


input = read_input("2024/day4", readlines=True)

input_matrix = [list(line.strip()) for line in input]

directions = {"right": (0, 1),
              "left": (0, -1),
              "down": (1, 0),
              "up": (-1, 0),
              "down_right": (1, 1),
              "up_left": (-1, -1),
              "down_left": (1, -1),
              "up_right": (-1, 1)
}

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
                for dx, dy in directions.values():
                    if check_direction(i, j, dx, dy, word, matrix):
                        xmas_count += 1
    return xmas_count

def check_x_mas(x, y, matrix):
    x_directions = ["down_right","up_left", "down_left",  "up_right"]
    counter = {"M": 0, "S": 0}
    
    for direction in x_directions:
        dx, dy = directions[direction]
        nx, ny = x + 1 * dx, y + 1 * dy
        if is_valid(nx, ny, matrix) and matrix[nx][ny] == "S":
            counter["S"] +=1
            nx, ny = x + 1 * dx * -1, y + 1 * dy * -1
            if is_valid(nx, ny, matrix) and matrix[nx][ny] == "M":
                counter["M"] +=1
            
    return counter["M"] == 2 and counter["S"] == 2


def count_x_words(matrix):
    xmas_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "A" and check_x_mas(i, j, matrix):
                xmas_count += 1
    return xmas_count

total = count_words(input_matrix)
print("Total XMASes: ", total)
x_total = count_x_words(input_matrix)
print("Total X-MASes: ", x_total)