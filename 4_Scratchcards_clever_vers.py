



total_1: int = 0

# part one solution
with open('Advent_of_code_2023/data/input_day_4.txt', 'r') as file:

    for line in file:
        line = line.split(':')[1].strip()
        left, right = line.split(" | ")

        winners = set(left.split())
        ours = set(right.split())

        matches = len(winners & ours)

        if matches > 0:
            total_1 += 2 ** (matches - 1)
    print(total_1)


# part two solution
lines = open('Advent_of_code_2023/data/input_day_4.txt',
             'r').read().splitlines()

counts = [1] * len(lines)

for i, line in enumerate(lines):
    line = line.split(':')[1].strip()
    left, right = line.split(" | ")

    matches = len(set(left.split()) & set(right.split()))
    print(matches)

    for n in range(i + 1, i + matches + 1):
        counts[n] += counts[i]

print(sum(counts))
