from collections import deque


PILES_DOWN: set[str] = 'S|JL'
PILES_UP: set[str] = 'S|7F'
PILES_LEFT: set[str] = 'S-J7'
PILES_RIGHT: set[str] = 'S-LF'


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

    # Thanks to HyperNeutrino

    start = find_S(grid)

    queue = deque([start])
    seen: set[tuple[int, int]] = set()

    seen.add(start)

    while queue:

        ver, hor = queue.popleft()
        curr_char = grid[ver][hor]

        if (ver > 0 and curr_char in PILES_DOWN and
           grid[ver-1][hor] in '|7F' and (ver-1, hor) not in seen):
            seen.add((ver-1, hor))
            queue.append((ver-1, hor))

        if (ver < len(grid) - 1 and curr_char in PILES_UP and
           grid[ver+1][hor] in '|JL' and (ver+1, hor) not in seen):
            seen.add((ver+1, hor))
            queue.append((ver+1, hor))

        if (hor > 0 and curr_char in PILES_LEFT and
           grid[ver][hor-1] in '-LF' and (ver, hor-1) not in seen):
            seen.add((ver, hor-1))
            queue.append((ver, hor-1))

        if (hor < len(grid[ver]) - 1 and curr_char in PILES_RIGHT and
           grid[ver][hor+1] in '-J7' and (ver, hor+1) not in seen):
            seen.add((ver, hor+1))
            queue.append((ver, hor+1))

    return len(seen) // 2


def second_round(grid: list[list[str]]) -> int:
    pass


print(first_round(read_input()))
# print(second_round(read_input()))
