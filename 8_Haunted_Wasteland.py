from math import gcd


LEFT_RIGHT: dict = {'L': 0, 'R': 1}


def read_input() -> tuple[list[str], dict[str: list[str]]]:
    with open('Advent_of_code_2023/data/input_day_8.txt', 'r') as file:

        instructions: list[str] = list(file.readline().strip())
        path: dict[str: list[str]] = {}

        file.readline()

        for line in file:
            line = line.rstrip('\n').split('=')
            start, choices = (line[0].strip(),
                              line[1].lstrip(' (').rstrip(')').split(', '))
            path[start] = choices

    return (instructions, path)


def first_round(instructions: list[str], path: dict[str: list[str]]) -> int:

    index: int = 0
    cur = 'AAA'

    while cur != 'ZZZ':
        cur = path[cur][LEFT_RIGHT[instructions[index % len(instructions)]]]
        index += 1

    return index


def second_round(instructions: list[str], path: dict[str: list[str]]) -> int:

    def find_all_ends_A(path) -> list[str]:

        starts: list[str] = []

        for key in path.keys():
            if key[2] == 'A':
                starts.append(key)

        return starts

    def find_length_cycle(start: str, path) -> int:

        index: int = 0

        while not start.endswith('Z'):
            start = path[start][LEFT_RIGHT[instructions[
                index % len(instructions)
            ]]]
            index += 1

        return index

    starts = find_all_ends_A(path)

    cycles: list[int] = [find_length_cycle(start, path) for start in starts]
    lcn: int = 1

    for cycle in cycles:
        lcn = lcn * cycle // gcd(lcn, cycle)

    return lcn


# print(first_round(*read_input()))
print(second_round(*read_input()))
