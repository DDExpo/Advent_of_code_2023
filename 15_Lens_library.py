

def hash_char(key: str) -> int:

    global boxes
    global cach

    if key in cach:
        return cach[key]

    res: int = 0

    for char in key:
        res += ord(char)
        res *= 17
        res %= 256

    cach[key] = res

    return res


long_fucking_line = open(
    'Advent_of_code_2023/data/input_day_15.txt', 'r'
).read().strip().split(',')

boxes: list[dict[str: int]] = [{} for _ in range(256)]
cach: dict[str: int] = {}
result: int = 0

for lens in long_fucking_line:
    if '-' in lens:
        key = lens[:-1]
        box = boxes[hash_char(key)]
        if key in box:
            box.pop(key)
    else:
        key = lens[:-2]
        box = boxes[hash_char(key)]
        box[key] = lens[-1]

for number_box, box in enumerate(boxes):
    order_lens = 1
    for key, val in box.items():
        result += (number_box+1) * order_lens * int(val)
        order_lens += 1

print(result)
