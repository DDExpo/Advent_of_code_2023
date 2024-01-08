

# Only final solution - for part two is remained


with open('Advent_of_code_2023/data/input_day_2.txt', 'r') as file:
    sum_max_cubes: int = 0

    for line in file:
        id, games = line.rstrip('\n').lstrip('Game').split(':')
        sum_cubes: int = 1
        games: list[str] = games.split(';')
        max_cubes: dict[str: int] = {'red': 0, 'green': 0, 'blue': 0}

        for game in games:
            cubes = game.strip(' ').split(', ')
            for cube in cubes:
                amount, colour = cube.split(' ')
                max_cubes[colour] = max(max_cubes[colour], int(amount))
        for val in max_cubes.values():
            sum_cubes *= val
        sum_max_cubes += sum_cubes
    print(sum_max_cubes)
