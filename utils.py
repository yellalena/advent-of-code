import os

def read_input(filepath, filename: str = "input.txt", readlines = False) -> str:
    with open(os.path.join(filepath, filename), "r") as file:
        if readlines:
            input_lines = file.readlines()
        else:
            input_lines = file.read()
    return input_lines
