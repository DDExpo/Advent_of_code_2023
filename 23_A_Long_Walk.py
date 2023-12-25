

hike_map: list[str] = open('Advent_of_code_2023/data/input_day_23.txt'
                           ).read().splitlines()

start, end = (0, 1), (len(hike_map)-1, len(hike_map[0])-2)
points: list[tuple[int, int]] = [start, end]
dirs: dict[str: list[tuple[int, int]]] = {
    'v': [(1, 0)], '>': [(0, 1)], '<': [(0, -1)], '^': [(-1, 0)],
    '.': [(-1, 0), (0, 1), (0, -1), (1, 0)]
}

#                                                     '#.#'
# so firstly we find all points where we have 3> ways '.*.' to go, point=(1, 1)
#                                                     '#.#'
#                                        '.######'
# When we compress our paths from        '......#'
# to 'start = (0, 0), nearest pt (3, 5)  '#####.#'
#                                        '.....*.'
#                                        '.####.#'
for y, row in enumerate(hike_map):
    for x, ch in enumerate(row):
        if ch == '#':
            continue
        neighbors = 0
        for ny, nx in [(y, x-1), (y+1, x), (y, x+1), (y-1, x)]:
            if (0 <= ny < len(hike_map) and 0 <= nx < len(hike_map[0])
               and hike_map[ny][nx] != '#'):
                neighbors += 1
        if neighbors >= 3:
            points.append((y, x))


# After this we create directed graph
graph: dict[tuple[int, int]: dict] = {pt: {} for pt in points}

for sy, sx in points:
    stack = [(0, sy, sx)]
    seen = {(sy, sx)}

    while stack:

        n, y, x = stack.pop()

        if n != 0 and (y, x) in points:
            graph[(sy, sx)][(y, x)] = n
            continue

        # Part one
        # for dy, dx in dirs[hike_map[y][x]]:

        # Part two
        for dy, dx in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < len(hike_map) and 0 <= nx < len(hike_map[0])
               and hike_map[ny][nx] != '#' and (ny, nx) not in seen):
                stack.append((n + 1, ny, nx))
                seen.add((ny, nx))

seen = set()


# When we just recursivly brute force through graph to fined the longest one
def dfs(pt):

    if pt == end:
        return 0

    m = float('-inf')

    seen.add(pt)
    for npt in graph[pt]:
        if npt not in seen:
            m = max(m, dfs(npt) + graph[pt][npt])
    seen.remove(pt)

    return m


print(dfs(start))
