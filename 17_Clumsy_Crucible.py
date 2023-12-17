import heapq
from pprint import pprint


def find_the_least_heated_path(city: list[list[int]]) -> int:

    queue: list[tuple[int, int]] = [(0, 0, 0, 0, 0, 0)]
    visited: set[tuple[int, int]] = set()

    while queue:
        hl, y, x, dy, dx, ns = heapq.heappop(queue)

        # 'and ns >= 4': Part two
        if y == len(city) - 1 and x == len(city[0]) - 1 and ns >= 4:
            print(hl)
            break

        if (y, x, dy, dx, ns) in visited:
            continue

        visited.add((y, x, dy, dx, ns))

        # ns < 3 to ns < 10: Part two
        if ns < 10 and (dy, dx) != (0, 0):
            nx = x + dx
            ny = y + dy
            if 0 <= ny < len(city) and 0 <= nx < len(city[0]):
                heapq.heappush(queue,
                               (hl + city[ny][nx], ny, nx, dy, dx, ns + 1))

        if ns >= 4 or (dy, dx) == (0, 0):  # Part Two
            for ndy, ndx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndy, ndx) != (dy, dx) and (ndy, ndx) != (-dy, -dx):
                    nx = x + ndx
                    ny = y + ndy
                    if 0 <= ny < len(city) and 0 <= nx < len(city[0]):
                        heapq.heappush(
                            queue, (hl + city[ny][nx], ny, nx, ndy, ndx, 1)
                        )


city: list[list[int]] = [list(map(int, line)) for line
                         in open('Advent_of_code_2023/data/input_day_17.txt',
                                 'r').read().split('\n')]
city.pop()
pprint(city, compact=True)
find_the_least_heated_path(city)
