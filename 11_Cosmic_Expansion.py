from time_exucute import time_excution


def read_input() -> list[list[str]]:
    with open('Advent_of_code_2023/data/input_day_11.txt', 'r') as file:

        grid: list[list[str]] = []

        for line in file:
            grid.append(line.strip())

    return grid


@time_excution
def better_solution(galaxy: list[list[str]], scale: int):

    def construct_psa(galaxy) -> list[int]:
        psa = [0 for _ in range(len(galaxy) + 1)]
        for i, row in enumerate(galaxy):
            psa[i] = (psa[i - 1] + (scale if all(x == '.'
                                                 for x in row) else 1))
        return psa

    row_psa: list[int] = construct_psa(galaxy)
    col_psa: list[int] = construct_psa(list(zip(*galaxy)))

    galaxies: list[tuple[int, int]] = []

    for r, row in enumerate(galaxy):
        for c, ch in enumerate(row):
            if ch == '#':
                galaxies.append((r, c))

    total: int = 0

    for i, (r1, c1) in enumerate(galaxies):
        for r2, c2 in galaxies[:i]:
            total += row_psa[max(r1, r2)] - row_psa[min(r1, r2)]
            total += col_psa[max(c1, c2)] - col_psa[min(c1, c2)]

    print(total)


@time_excution
def even_better_solution(galaxy: list[list[str]], scale: int):

    def construct_psa(galaxy) -> list[int]:
        psa = [0 for _ in range(len(galaxy) + 1)]
        for i, row in enumerate(galaxy):
            psa[i] = (psa[i - 1] + (scale if all(x == '.'
                                                 for x in row) else 1))
        return psa

    row_psa: list[int] = construct_psa(galaxy)
    col_psa: list[int] = construct_psa(list(zip(*galaxy)))

    rows: list[tuple[int, int]] = []
    cols: list[tuple[int, int]] = []

    for r, row in enumerate(galaxy):
        count = row.count('#')
        if count > 0:
            rows.append((r, count))

    for c, col in enumerate(zip(*galaxy)):
        count = col.count('#')
        if count > 0:
            cols.append((c, count))

    total: int = 0

    def compute(indexies, psa) -> int:
        cumulative: int = 0
        num_seen: int = 0
        total: int = 0
        for index, count in indexies:
            total += (num_seen * psa[index] - cumulative) * count
            cumulative += psa[index] * count
            num_seen += count
        return total

    total += compute(rows, row_psa)
    total += compute(cols, col_psa)
    print(total)


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


@time_excution
def count_empty_space(galaxy: list[list[str]], scale: int) -> int:

    empty_spaces, position = fake_expanding_galaxy_find_all(galaxy)
    result: int = 0

    for start in range(len(position)):
        s = position[start]
        for goal in range(start+1, len(position)):
            g = position[goal]
            distance = abs(s[0]-g[0]) + abs(s[1]-g[1])
            for i in range(min(s[0], g[0])+1, max(s[0], g[0])):
                if i not in empty_spaces[0]:
                    distance += scale - 1
            for i in range(min(s[1], g[1])+1, max(s[1], g[1])):
                if i not in empty_spaces[1]:
                    distance += scale - 1
            result += distance

    return result


galaxy = read_input()
print(count_empty_space(galaxy, scale=2))
print(count_empty_space(galaxy, scale=1000000))

better_solution(galaxy, scale=2)
better_solution(galaxy, scale=1000000)

even_better_solution(galaxy, scale=2)
even_better_solution(galaxy, scale=1000000)
