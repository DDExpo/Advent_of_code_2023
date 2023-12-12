

cache = {}


def recursive(hot_springs: list[str], map_hot: tuple[int]) -> int:

    # Big thanks to HyperNeutrino

    if hot_springs == '':
        return 1 if map_hot == () else 0

    if map_hot == ():
        return 0 if '#' in hot_springs else 1

    key = (hot_springs, map_hot)

    if key in cache:
        return cache[key]

    result: int = 0

    if hot_springs[0] in '.?':
        result += recursive(hot_springs[1:], map_hot)

    if hot_springs[0] in '#?':
        if (map_hot[0] <= len(hot_springs) and '.' not in
            hot_springs[:map_hot[0]] and (map_hot[0] == len(hot_springs)
                                          or hot_springs[map_hot[0]] != '#')):
            result += recursive(hot_springs[map_hot[0] + 1:], map_hot[1:])

    cache[key] = result
    return result


with open('Advent_of_code_2023/data/input_day_12.txt', 'r') as file:

    result: int = 0

    for line in file:
        hot_springs, map_hot = line.strip().split()
        map_hot = tuple(map(int, map_hot.split(',')))

        # Part two
        map_hot *= 5
        hot_springs = '?'.join([hot_springs]*5)

        result += recursive(hot_springs, map_hot)

    print(result)
