

SYMBOLS: set[str] = set(',+-=@!.&$%#/')
SUM_ENGINE_NUMS: int = 0
skip: int = 0


file = open('Adventofcode/data/input_day_3.txt', 'r').read().splitlines()


def traverse_to_end_num(col: int, row: int,
                        m_row: int) -> tuple[int, int]:

    row_l: int = row - 1 if row - 1 > 0 else 0
    row_r: int = row + 1 if row < len(file[0]) else len(file[0]) - 1

    if file[col][row_l].isdigit() and file[col][row_r].isdigit():
        return (int(''.join(file[col][row_l: row_r+1])), (m_row-row_r +
                                                          (row_r-row+1)))

    elif file[col][row_l].isdigit():
        while row_l != 0 and file[col][row_l-1].isdigit():
            row_l -= 1
        return (int(''.join(file[col][row_l: row+1])), 0)
    elif file[col][row_r].isdigit():
        while row_r != len(file[0]) - 1 and file[col][row_r+1].isdigit():
            row_r += 1
        return (int(''.join(file[col][row: row_r+1])), (m_row-row_r +
                                                        (row_r-row+1)))
    else:
        return (int(file[col][row]), 0)


def has_two_numbers_in_radius_one(col: int, row: int) -> int:

    sum_num: int = 1
    count: int = 2
    skip: int = 0
    end: int = row

    col_up = col - 1 if col - 1 > 0 else 0
    col_down = col + 1 if col + 1 < len(file) else len(file)-1
    row_serch = row - 1 if row - 1 > 0 else 0
    end_search = end + 1 if end + 1 < len(file[0]) else len(file[0])-1

    for ver in range(col_up, col_down+1):
        for hor in range(row_serch, end_search+1):
            if file[ver][hor].isdigit() and skip == 0:
                count -= 1
                if count >= 0:
                    num, skip = traverse_to_end_num(ver, hor, row)
                    sum_num *= num
                else:
                    return 0
            elif skip > 0:
                skip -= 1
    if count == 1:
        return 0

    return sum_num


for i, column in enumerate(file):
    for j, row in enumerate(column):
        if row in SYMBOLS or row.isdigit():
            continue

        if row == '*':
            SUM_ENGINE_NUMS += has_two_numbers_in_radius_one(i, j)

print(SUM_ENGINE_NUMS)
