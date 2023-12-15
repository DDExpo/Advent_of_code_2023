from pprint import pprint


def rotate_the_wall_part_one():

    wall: list[list[str]] = []

    with open('Advent_of_code_2023/data/input_day_14.txt', 'r') as file:

        for line in file:
            wall.append(list(line.strip()))

    rocks: list[int] = [0] * len(wall[0])
    result: int = 0

    for i in range(len(wall)-1, -1, -1):
        for j, objects in enumerate(wall[i]):

            if objects == '#' or i == 0:
                index = i

                if objects == '.':
                    while rocks[j] > 0:
                        rocks[j] -= 1
                        wall[index][j] = 'O'
                        result += 100 - index
                        index += 1

                elif objects == 'O':
                    result += 100
                    index += 1
                    while rocks[j] > 0:
                        rocks[j] -= 1
                        wall[index][j] = 'O'
                        result += 100 - index
                        index += 1

                else:
                    while rocks[j] > 0:
                        rocks[j] -= 1
                        index += 1
                        result += 100 - index
                        wall[index][j] = 'O'

            elif objects == 'O' and i > 0:
                wall[i][j] = '.'
                rocks[j] += 1

    wall = [''.join(wall_level) for wall_level in wall]

    print(result)
    pprint(wall)


def HyperNeutrino_solution_part_one():

    wall = open('Advent_of_code_2023/data/test.txt').read().splitlines()
    # rotated the wall at 90 degree, so north now is right
    new_wall = list(map(''.join, zip(*wall)))
    pprint(list(zip(new_wall, wall)), compact=True, width=34)

    new_wall = ['#'.join([''.join(sorted(list(group), reverse=True)) for group
                          in row.split('#')]) for row in new_wall]
    print('__________________________________')

    pprint(list(zip(new_wall, wall)), compact=True, width=34)
    new_wall = list(map(''.join, zip(*new_wall)))

    print(sum(row.count('O') * (len(new_wall) - index)
              for index, row in enumerate(new_wall)))


wall = tuple(open(
    'Advent_of_code_2023/data/input_day_14.txt'
).read().splitlines())


def HyperNeutrino_solution_part_two():

    global wall

    def cycle():
        global wall
        for _ in range(4):
            wall = tuple(map(''.join, zip(*wall)))
            wall = tuple('#'.join([''.join(sorted(tuple(group), reverse=True))
                         for group in row.split('#')]) for row in wall)
            wall = tuple(row[::-1] for row in wall)

    seen: set[tuple[str]] = {wall}
    array: list[tuple[str]] = [wall]
    iter: int = 0

    while True:
        iter += 1
        cycle()
        if wall in seen:
            break
        seen.add(wall)
        array.append(wall)

    start = array.index(wall)
    print(iter, start)
    wall = array[(1000000000 - start) % (iter - start) + start]

    print(sum(row.count('O') * (len(wall) - index)
              for index, row in enumerate(wall)))


rotate_the_wall_part_one()
HyperNeutrino_solution_part_one()
HyperNeutrino_solution_part_two()
