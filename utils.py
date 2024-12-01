import os

def read_input(filepath, filename: str = "input.txt") -> str:
    with open(os.path.join(filepath, filename), "r") as file:
        input_lines = file.read()
    return input_lines
