from collections import deque


bricks = [list(map(int, line.replace('~', ',').split(','))) for line
          in open('Advent_of_code_2023/data/input_day_22.txt')]

# We start with simulating the falling of bricks
bricks.sort(key=lambda x: x[2])


def overlaps(a: list[int], b: list[int]) -> bool:
    return (max(a[0], b[0]) <= min(a[3], b[3]) and
            max(a[1], b[1]) <= min(a[4], b[4]))


for i, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:i]:
        if overlaps(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

bricks.sort(key=lambda x: x[2])

# then we create back to back mapping by indexies for every brick what overlaps
k_supports_v: dict[int: set[int]] = {i: set() for i in range(len(bricks))}
v_supports_k: dict[int: set[int]] = {i: set() for i in range(len(bricks))}

for i, upper in enumerate(bricks):
    for ii, lower in enumerate(bricks[:i]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[ii].add(i)
            v_supports_k[i].add(ii)

total: int = 0

# then we iterate through it and add +1
# for all bricks what have more than one overlaps
# Part One
# for i in range(len(bricks)):
#     if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
#         total += 1


# Part two
for i in range(len(bricks)):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)  # so we dont count disentagrated bricks

    while q:
        j = q.popleft()
        for k in k_supports_v[j] - falling:
            if v_supports_k[k] <= falling:
                q.append(k)
                falling.add(k)
    total += len(falling) - 1


print(total)
