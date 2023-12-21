from collections import deque


def read_input() -> tuple[list[str], tuple[int, int]]:
    garden: list[str] = []
    start: tuple[int, int] = ()
    with open('Advent_of_code_2023/data/input_day_21.txt') as file:

        for i, line in enumerate(file):
            if 'S' in line:
                start = (i, line.find('S'))

            garden.append(line.strip())

    return (garden, start)


# recursve doesnt work fuck
def count_steps_bad(garden: list[str], start: tuple[int, int], steps: int):

    seen: set[tuple[int, int]] = set()
    seen.add(start)

    def dfs(cur, steps):

        y, x = cur

        if steps == 0:
            return

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dy = (y + dy if 0 <= (y + dy) < len(garden)
                  else min(max(0, y+dy), len(garden) - 1))
            dx = (x + dx if 0 <= (x + dx) < len(garden[0])
                  else min(max(0, x+dx), len(garden) - 1))

            if garden[dy][dx] == '#' or (dy, dx) in seen:
                continue

            if (abs(start[0]-dy) + abs(start[1]-dx)) % 2 == 0:
                seen.add((dy, dx))
                garden[dy][dx] = 'O'

            dfs((dy, dx), steps-1)

    if steps % 2 == 0:
        garden[start[0]][start[1]] = 'O'

    dfs(start, steps)


# youtube - HyperNeutrino
def count_steps_good(ans, seen, queue, garden: list[str]):

    while queue:

        y, x, steps = queue.popleft()

        if steps % 2 == 0:
            ans.add((y, x))

        if steps == 0:
            continue

        for ny, nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
            if (ny < 0 or ny > len(garden) or nx < 0 or nx > len(garden[0])
               or garden[ny][nx] == '#' or (ny, nx) in seen):
                continue
            seen.add((ny, nx))
            queue.append((ny, nx, steps-1))

    print(len(ans))


garden, start = read_input()
ans: set[tuple[int, int]] = set()
seen: set[tuple[int, int]] = set((start[0], start[1]))
queue = deque([(start[0], start[1], 26501365)])

count_steps_good(ans, seen, queue, garden)
