

values, *rest = open('Advent_of_code_2023/data/input_day_5.txt').read().split('\n\n')

values = list(map(int, values.split(':')[1].strip().split()))


# Part one solution
for block in rest:

    _, *lines = block.splitlines()
    lines = [list(map(int, line.split())) for line in lines]

    mapped = []

    for value in values:
        for t_range_s, s_range_s, range_l in lines:
            if s_range_s <= value < s_range_s + range_l:
                mapped.append(value + t_range_s - s_range_s)
                break
        else:
            mapped.append(value)

    seed = mapped

print(min(mapped))


# Part two solution
intervals = [(values[i], values[i] + values[i+1]) for i in range(len(0, len(values), 2))]

for block in rest:

    _, *lines = block.splitlines()
    lines = [list(map(int, line.split())) for line in lines]

    mapped = []

    for inter_s, inter_e in intervals:
        for t_range_s, s_range_s, range_l in lines:
            s_range_e = s_range_s + range_l
            over_s = max(inter_s, s_range_s)
            over_e = min(inter_e, s_range_e)
            if over_e > over_s:
                mapped.append((over_s + t_range_s - s_range_s, over_e + t_range_s - s_range_s))
                if over_s > inter_s:
                    intervals((inter_s, over_s))
                if inter_e > over_e:
                    intervals.append((over_e, inter_e))
                break
        else:
            mapped.append((inter_s, inter_e))
    intervals = mapped

print(min(mapped)[0])
