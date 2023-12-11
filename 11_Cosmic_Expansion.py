

def read_input() -> list[list[str]]:
    with open('Advent_of_code_2023/data/input_day_11.txt', 'r') as file:

        grid: list[list[str]] = []

        for line in file:
            grid.append(line.strip())

    return grid


def fake_expanding_galaxy_find_all(
        galaxy: list[list[str]]
        ) -> tuple[tuple[set[int], set[int]], list[tuple[int, int]]]:

    empty_space_hor: set[int] = set()
    empty_space_ver: set[int] = set()
    position: list[tuple[int, int]] = []

    for x, row in enumerate(galaxy):
        for y, object in enumerate(row):
            if object == '#':
                position.append((x, y))
                empty_space_ver.add(y)
                empty_space_hor.add(x)

    return ((empty_space_hor, empty_space_ver), position)


def first_round(galaxy: list[list[str]]) -> int:

    empty_spaces, position = fake_expanding_galaxy_find_all(galaxy)
    result: int = 0

    for start in range(len(position)):
        s = position[start]
        for goal in range(start+1, len(position)):
            g = position[goal]
            distance = abs(s[0]-g[0]) + abs(s[1]-g[1])
            for i in range(min(s[0], g[0])+1, max(s[0], g[0])):
                if i not in empty_spaces[0]:
                    distance += 1
            for i in range(min(s[1], g[1])+1, max(s[1], g[1])):
                if i not in empty_spaces[1]:
                    distance += 1
            result += distance

    return result


def second_round(galaxy: list[list[str]]) -> int:

    empty_spaces, position = fake_expanding_galaxy_find_all(galaxy)
    result: int = 0

    for start in range(len(position)):
        s = position[start]
        for goal in range(start+1, len(position)):
            g = position[goal]
            distance = abs(s[0]-g[0]) + abs(s[1]-g[1])
            for i in range(min(s[0], g[0])+1, max(s[0], g[0])):
                if i not in empty_spaces[0]:
                    distance += 999999
            for i in range(min(s[1], g[1])+1, max(s[1], g[1])):
                if i not in empty_spaces[1]:
                    distance += 999999
            result += distance

    return result


galaxy = read_input()
# print(first_round(galaxy))
print(second_round(galaxy))
