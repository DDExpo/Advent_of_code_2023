

# Only final solution - for part two is remained


DICT = {'o': {'n': {'e': 'L'}}, 't': {'w': {'o': 'L'},
                                      'h': {'r': {'e': {'e': 'L'}}}},
        'f': {'o': {'u': {'r': 'L'}}, 'i': {'v': {'e': 'L'}}},
        's': {'i': {'x': 'L'}, 'e': {'v': {'e': {'n': 'L'}}}},
        'e': {'i': {'g': {'h': {'t': 'L'}}}}, 'n': {'i': {'n': {'e': 'L'}}}}

WORDS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def get_match_word_num(index: int, string: str,
                       is_last: bool = False) -> str | bool:

    if is_last:
        x = 3
        while x < 6:
            word = ''.join(reversed(string[index: index-x: -1]))
            if word in WORDS:
                return WORDS[word]
            x += 1
        return False

    word: str = string[index]
    temp_dict: dict[dict[str]] | str = DICT[string[index]]

    while temp_dict != 'L':
        index += 1
        if temp_dict.get(string[index]):
            word += string[index]
            temp_dict = temp_dict[string[index]]
        else:
            break

    if word in WORDS:
        return WORDS[word]
    return False


def first_match(string: str) -> str:

    for i in range(len(string)):

        if string[i].isdigit():
            return string[i]
        elif string[i] in DICT:
            res = get_match_word_num(i, string)
            if res:
                return res


def last_match(string: str) -> str:

    for i in range(len(string)-1, -1, -1):

        if string[i].isdigit():
            return string[i]
        elif string[i] in DICT or string[i] in 'eorxnt':
            res = get_match_word_num(i, string, True)
            if res:
                return res


with open(
    'Advent_of_code_2023/data/adventofcode.com_2023_day_1_input.txt', 'r'
) as file:

    sum_digits: int = 0
    for line in file:
        line = line.strip('\n')
        result = first_match(line)+last_match(line)
        sum_digits += int(result)
    print(sum_digits)
