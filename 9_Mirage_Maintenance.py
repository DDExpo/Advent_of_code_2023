

def recursive(nums: list[int]) -> int:
    # thanks to HyperNeutrino, i am too fucking stupid for this problem

    if all(num == 0 for num in nums):
        return 0
    deltas = [y - x for x, y in zip(nums, nums[1:])]
    diff = recursive(deltas)

    return nums[-1] + diff


def recursive_2(nums: list[int]) -> int:
    # Big thanks to HyperNeutrino

    if all(num == 0 for num in nums):
        return 0
    deltas = [y - x for x, y in zip(nums, nums[1:])]
    diff = recursive_2(deltas)

    return nums[0] - diff


result: int = 0

with open('Advent_of_code_2023/data/input_day_9.txt', 'r') as file:

    for line in file:
        line = [int(n) for n in line.strip().split()]
        result += recursive_2(line)

print(result)
