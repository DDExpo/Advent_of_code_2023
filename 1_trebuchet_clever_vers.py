import re


# First part solution
def first_digit(line):
    # return [ch for ch in line if ch.isdigit()][0]
    return re.search('\\d', line).group()


def last_digit(line):
    # return [ch for ch in line if ch.isdigit()][-1]
    # return re.search('.*(\\d)', line[::-1]).group()
    return re.search('.*(\\d)', line).group(1)

total_1: int = 0
total_2: int = 0

# Second part solution
translations = []

for i, digit in enumerate('one two three four five six seven eight nine'.split(), 1):
    translations.append((digit, f'{digit[0]}{i}{digit[-1]}'))


# input
for line in open('Advent_of_code_2023/data/adventofcode.com_2023_day_1_input.txt'):

    # first part
    first = first_digit(line)
    last = last_digit(line)
    total_1 += int(first + last)

    # Second part
    for source, target in translations:
        line = line.replace(source, target)
    
    first = first_digit(line)
    last = last_digit(line)
    total_2 += int(first + last)

print(total_1)
print(total_2)
