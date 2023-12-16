

def lava_path_producing(
        cave: list[str],
        start: tuple[int, int, int, int] = (0, -1, 0, 1)
) -> int:

    # i just fucking give up on this bfs implementaion
    # these fuckig 60 lines of if else
    # so i looked up HyperNeutrino implementation

    visited: set[tuple[int, int]] = set()
    queue: list[tuple[int, int, int, int]] = [start]

    while queue:
        y, x, dy, dx = queue.pop()

        y += dy
        x += dx

        if y < 0 or y >= len(cave) or x < 0 or x >= len(cave[0]):
            continue

        ch = cave[y][x]

        if ch == '.' or (ch == '-' and dx != 0) or (ch == '|' and dy != 0):
            if (y, x, dy, dx) not in visited:
                queue.append((y, x, dy, dx))
                visited.add((y, x, dy, dx))

        elif ch == '/':
            dy, dx = -dx, -dy
            if (y, x, dy, dx) not in visited:
                queue.append((y, x, dy, dx))
                visited.add((y, x, dy, dx))

        elif cave[y][x] == '\\':
            dy, dx = dx, dy
            if (y, x, dy, dx) not in visited:
                queue.append((y, x, dy, dx))
                visited.add((y, x, dy, dx))

        else:
            for dy, dx in [(1, 0), (-1, 0)] if ch == '|' else [(0, 1),
                                                               (0, -1)]:
                if (y, x, dy, dx) not in visited:
                    queue.append((y, x, dy, dx))
                    visited.add((y, x, dy, dx))

    cords = {(y, x) for (y, x, _, _) in visited}

    return len(cords)


cave = open('Advent_of_code_2023/data/input_day_16.txt',
            'r').read().strip().split('\n')

# first part
print(lava_path_producing(cave))

# second part
result: int = 0

for y in range(len(cave)):
    result = max(result, lava_path_producing(cave, start=(y, -1, 0, 1)),
                 lava_path_producing(cave, start=(y, len(cave[0]), 0, -1)))

for x in range(len(cave)):
    result = max(result, lava_path_producing(cave, start=(-1, x, 1, 0)),
                 lava_path_producing(cave, start=(len(cave), x, -1, 0)))

print(result)
