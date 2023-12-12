

from pprint import pprint


def combos(hot_springs: list[str]) -> list[str]:

    if hot_springs == '':
        return ['']

    return [x + y for x in ('#.' if hot_springs[0] == '?' else hot_springs[0])
            for y in combos(hot_springs[1:])]


with open('Advent_of_code_2023/data/test.txt', 'r') as file:

    for line in file:
        hot_springs, map_hot = line.strip().split()
        map_hot = tuple(map(int, map_hot.split(',')))

        pprint(combos(hot_springs))
