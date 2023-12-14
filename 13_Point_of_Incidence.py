

def find_mirror(pattern: list[str]) -> int:

    # Big thanks to HyperNeutrino

    for row in range(1, len(pattern)):
        above = pattern[:row][::-1]
        below = pattern[row:]

        # first part
        # above = above[:below]
        # below = below[:above]

        # if above == below:
        #     return row

        # Part Two
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y))
               for x, y in zip(above, below)) == 1:
            return row

    return 0


result: int = 0

for block in open(
    'Advent_of_code_2023/data/input_day_13.txt'
).read().split('\n\n'):

    pattern = block.splitlines()

    rows = find_mirror(pattern)
    columns = find_mirror(list(zip(*pattern)))
    result += columns + 100 * rows

print(result)
