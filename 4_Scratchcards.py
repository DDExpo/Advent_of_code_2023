

SUM_WINNING_CARDS: int = 0


with open('Advent_of_code_2023/data/input_day_4.txt', 'r') as file:

    num_wins: list[int] = [1] * 202
    for i, line in enumerate(file):
        line = line.lstrip('Card ').rstrip('\n').split('|')
        winning_nums, nums = line[0].split()[1:], line[1].split()

        def first_round(win_nums: list[str], nums: list[str]) -> None:
            global SUM_WINNING_CARDS
            count: list[int] = [0] * 100
            total: int = 0

            for num in nums:
                count[int(num)] += 1

            for w_num in win_nums:
                count[int(w_num)] += 1
                if count[int(w_num)] >= 2:
                    if total == 0:
                        total += 1
                    else:
                        total *= 2

            SUM_WINNING_CARDS += total
            return

        # this slow as fuck
        def second_round(win_nums: list[str], nums: list[str], i: int) -> None:
            global SUM_WINNING_CARDS
            global num_wins
            count: list[int] = [0] * 100
            total: int = 0

            for num in nums:
                count[int(num)] += 1

            for j in range(1, num_wins[i]+1):
                if j > 1:
                    for k in range(i+1, i+total+1):
                        num_wins[k] += 1
                else:
                    for w_num in win_nums:
                        count[int(w_num)] += 1
                        if count[int(w_num)] == 2:
                            num_wins[i+j] += 1
                            j += 1
                            total += 1

            return num_wins[i]

        SUM_WINNING_CARDS += second_round(winning_nums, nums, i)

    print(SUM_WINNING_CARDS)
