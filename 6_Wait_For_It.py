

file = open('Advent_of_code_2023/data/input_day_6.txt',
            'r').read().splitlines()

times: list[str] = file[0][5:].strip().split()
distancies: list[str] = file[1][9:].strip().split()


def part_one(times: list[str], distancies: list[str]) -> int:

    times: list[int] = list(map(int, times))
    distancies: list[int] = list(map(int, distancies))

    sum_nums: int = 1
    for time, distance in zip(times, distancies):
        left = 1
        right = time
        l_f = r_f = True
        while l_f or r_f:
            if (time-left) * left <= distance:
                left += 1
            else:
                l_f = False
            if (time-right) * right <= distance:
                right -= 1
            else:
                r_f = False

        sum_nums *= right-left+1
    return sum_nums


# part_two
def part_two(times: list[str], distancies: list[str]) -> int:

    time: int = int(''.join(times))
    distance: int = int(''.join(distancies))

    left = 1
    right = time
    l_f = r_f = True
    while l_f or r_f:

        if (time-left) * left <= distance:
            left += 1
        else:
            l_f = False

        if (time-right) * right <= distance:
            right -= 1
        else:
            r_f = False

    return right-left+1


print(part_one(times, distancies))
print(part_two(times, distancies))
