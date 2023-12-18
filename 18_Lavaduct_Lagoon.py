

# Pick's theorem + shoelace formula
points: list[tuple[int, int]] = [(0, 0)]

dirs = {
    'U': (-1, 0), 'D': (1, 0),
    'R': (0, 1), 'L': (0, -1),
}

with open('Advent_of_code_2023/data/input_day_18.txt') as file:

    b: int = 0

    # Part one
    # for line in file:
    #     dir, steps, _ = line.strip().split()
    #     dy, dx = dirs[dir]
    #     steps = int(steps)
    #     b += steps
    #     y, x = points[-1]
    #     points.append((y + dy * steps, x + dx * steps))

    # Part two
    for line in file:
        _, _, hex = line.strip().split()
        x = hex[2:-1]
        dy, dx = dirs['RDLU'[int(x[-1])]]
        steps = int(x[:-1], 16)
        b += steps
        y, x = points[-1]
        points.append((y + dy * steps, x + dx * steps))

    A = abs(sum(points[i][0] *
                (points[i-1][1] - points[(i+1) % len(points)][1])
                for i in range(len(points)))) // 2

i: int = A - b//2 + 1

print(i + b)
