from collections import deque
import re

class CrateStack:
    def __init__(self):
        self.crates = deque()

    def push(self, item):
        self.crates.append(item)

    def pop(self):
        return self.crates.pop()

    @classmethod
    def fromlist(cls, list_value):
        new_stack = cls()
        new_stack.crates = deque(list_value)
        return new_stack
    
    def __repr__(self):
        return str(self.crates)

"""
***** initial crates state *****

    [V] [G]             [H]        
[Z] [H] [Z]         [T] [S]        
[P] [D] [F]         [B] [V] [Q]    
[B] [M] [V] [N]     [F] [D] [N]    
[Q] [Q] [D] [F]     [Z] [Z] [P] [M]
[M] [Z] [R] [D] [Q] [V] [T] [F] [R]
[D] [L] [H] [G] [F] [Q] [M] [G] [W]
[N] [C] [Q] [H] [N] [D] [Q] [M] [B]
 1   2   3   4   5   6   7   8   9 
"""

stacks = {
    1: CrateStack.fromlist(["N", "D", "M", "Q", "B", "P", "Z"]),
    2: CrateStack.fromlist(["C", "L", "Z", "Q", "M", "D", "H", "V"]),
    3: CrateStack.fromlist(["Q", "H", "R", "D", "V", "F", "Z", "G"]),
    4: CrateStack.fromlist(["H", "G", "D", "F", "N"]),
    5: CrateStack.fromlist(["N", "F", "Q"]),
    6: CrateStack.fromlist(["D", "Q", "V", "Z", "F", "B", "T"]),
    7: CrateStack.fromlist(["Q", "M", "T", "Z", "D", "V", "S", "H"]),
    8: CrateStack.fromlist(["M", "G", "F", "P", "N", "Q"]),
    9: CrateStack.fromlist(["B", "W", "R", "M"])
}

with open("day5_input.txt") as file:
    instructions = [
        [int(i) for i in re.findall(r'\d+', line)]
        for line in file.readlines()
    ]

for n_books, from_crate, to_crate in instructions:
    for i in range(n_books):
        stacks[to_crate].push(stacks[from_crate].pop())


result = ""
for stack in stacks.values():
    result += stack.pop()

print(result)