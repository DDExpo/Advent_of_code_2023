

from pprint import pprint


def roted_the_wall_text(wall: list[list[str]]) -> tuple[list[list[str]], int]:

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
    z = 0

    for s in wall:
        z += s.count('O')

    print(z)

    return (wall, result)


def first_part(rotated_wall: list[str]) -> int:
    pass


def second_part():
    pass


wall: list[list[str]] = []

with open('Advent_of_code_2023/data/input_day_14.txt', 'r') as file:

    for line in file:
        wall.append(list(line.strip()))

rotated_wall, result = roted_the_wall_text(wall)

# print(first_part(rotated_wall))
# print(second_part(rotated_wall))

pprint(rotated_wall)
print(result)
