

from pprint import pprint


MAP_OF_PILES: dict[str: tuple[int, int]] = {
    '|': (1, 0), '-': (0, 1), 'L': (0, +1), 'J': (+1, 0),
    '7': (0, -1), 'F': (-1, 0), '.': (0, 0)
}


def read_input() -> list[list[str]]:
    with open('Advent_of_code_2023/data/input_day_10.txt', 'r') as file:

        grid: list[list[str]] = []

        for line in file:
            grid.append(list(line.strip()))

    return grid


def find_S(grid) -> tuple[int, int]:

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'S':
                return (i, j)


def first_round(grid: list[list[str]]) -> int:

    start = find_S(grid)

    mouse1 = (start[0]+1, start[1])
    mouse2 = (start[0], start[1]-1)
    mouse3 = (start[0]+1, start[1]+1)

    steps: int = 1

    while mouse1 != mouse2 != mouse3:

        mouse1 = MAP_OF_PILES[grid[mouse1[0]][mouse1[1]]]
        mouse2 = (start[0], start[1]-1)
        mouse3 = (start[0]+1, start[1]+1)
        steps += 1

def second_round(grid: list[list[str]]) -> int:
    pass


print(first_round(read_input()))
print(second_round(read_input()))
