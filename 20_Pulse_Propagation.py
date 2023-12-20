import math
from collections import deque


def read_input() -> tuple[dict[str: tuple[int, str, list[str]]], list[str]]:
    with open('Advent_of_code_2023/data/input_day_20.txt') as file:

        web: dict[str: list[str]] = {}
        start: list[int] = []
        counts: dict[str: int] = {}

        for line in file:
            key, val = line.strip('\n').split(' -> ')
            if key == 'broadcaster':
                start = tuple(val.split(', '))
            else:
                web[key[1:]] = (key[0]+'-', tuple(val.split(', ')))
                if key[0] == '&':
                    counts[key[1:]] = 0

        for vals in list(web.values()):
            for val in vals[1]:
                if val in counts:
                    counts[val] += 1

        for key, val in counts.items():
            web[key] = (web[key][0], web[key][1], val)

    return (web, start)


# This is shit code what doesnt solve correctly and i dont know why
# so i just give up after seven hours, and yeah i wanna kms
def count_pulses(web: dict[str: tuple[int, str, list[str]]],
                 button_pushes: int,
                 start: list[str]):

    hl_01: dict[str: str] = {'+': '-', '-': '+', 0: 1, 1: 0}
    pulses_lh = [0, 0]

    # seen_scheme: set[dict[str: tuple[str, list[str]]]] = set()

    for _ in range(button_pushes):
        signal_h: int = 0
        fifo: deque[tuple(str, int)] = deque([(st, signal_h) for st in start])
        # if tuple(web.items()) in seen_scheme:
        #     break
        # seen_scheme.add(tuple(web.items()))
        while fifo:
            to_modules, signal_h = fifo.popleft()
            val = web[to_modules]
            pulses_lh[signal_h] += 1
            if val[0][0] == '%':
                if not signal_h:
                    for cur_model in val[1]:
                        if cur_model not in web:
                            pulses_lh[signal_h] += 1
                            continue
                        fifo.append((cur_model, signal_h))
                    web[to_modules] = ('%'+hl_01[val[0][1]], val[1])
                    signal_h = 0 if val[0][1] == '+' else 1
            else:
                if signal_h:
                    if val[2] == 1:
                        for cur_model in val[1]:
                            if cur_model not in web:
                                pulses_lh[signal_h-1] += 1
                                continue
                            fifo.append((cur_model, signal_h - 1))
                        web[to_modules] = (val[0], val[1], val[2] - 1)
                    else:
                        for cur_model in val[1]:
                            if cur_model not in web:
                                pulses_lh[signal_h] += 1
                                continue
                            fifo.append((cur_model, signal_h))
                        web[to_modules] = (val[0], val[1], val[2]-1)
                else:
                    for cur_model in val[1]:
                        if cur_model not in web:
                            pulses_lh[hl_01[signal_h]] += 1
                            continue
                        fifo.append((cur_model, hl_01[signal_h]))
                    signal_h = 0 if val[2] == 0 else 1
                    web[to_modules] = (val[0], val[1], val[2] + 1)

    print((pulses_lh[0]+1000) * (pulses_lh[1]))


# This is good solution, solution above is baaad one
# Big thanks to HyperNeutrino youtube-HyperNeutrino
class Module():
    def __init__(self, name: str, typpe: str, outputs: list[str]) -> None:
        self.name = name
        self.typpe = typpe
        self.outputs = outputs

        if self.typpe == '%':
            self.memory: str = 'off'
        else:
            self.memory: dict[str: str] = {}

    def __repr__(self) -> str:
        return (self.name + '{type=' + self.typpe + ', outputs=' +
                ','.join(self.outputs) + ', memory=' + str(self.memory) + '}')


modules: dict[str, Module] = {}
broadcast_targets: list[str] = []

for line in open('Advent_of_code_2023/data/input_day_20.txt'):
    left, right = line.strip().split(' -> ')
    outputs = right.split(', ')
    if left == 'broadcaster':
        broadcast_targets = outputs
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].typpe == '&':
            modules[output].memory[name] = 'lo'


def first_round(modules, broadcast_targets):
    lohi: dict[str: int] = {'lo': 0, 'hi': 0}

    for _ in range(1000):
        lohi['lo'] += 1
        q = deque([('broadcaster', x, 'lo') for x in broadcast_targets])

        while q:
            origin, target, pulse = q.popleft()
            lohi[pulse] += 1

            if target not in modules:
                continue

            module = modules[target]

            if module.typpe == '%':
                if pulse == 'lo':
                    module.memory = 'on' if module.memory == 'off' else 'off'
                    outgoing = 'hi' if module.memory == 'on' else 'lo'
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = ('lo' if all(x == 'hi' for x in
                                        module.memory.values()) else 'hi')
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

    lo, hi = lohi.values()
    print(lo * hi)


# This is some crazy shit
# It doesnt work for me :(
def second_round(modules, broadcast_targets):

    (feed,) = [name for name, module in modules.items()
               if 'rx' in module.outputs]
    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items()
            if feed in module.outputs}
    presses = 0

    while True:
        presses += 1
        q = deque([('broadcaster', x, 'lo') for x in broadcast_targets])

        while q:
            origin, target, pulse = q.popleft()

            if target not in modules:
                continue

            module = modules[target]

            if module.name == feed and pulse == 'hi':
                seen[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lengths[origin]

                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = x * cycle_length // math.gcd(x, cycle_length)
                    print(x)
                    exit(0)

            if module.typpe == '%':
                if pulse == 'lo':
                    module.memory = 'on' if module.memory == 'off' else 'off'
                    outgoing = 'hi' if module.memory == 'on' else 'lo'
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = ('lo' if all(x == 'hi' for x in
                                        module.memory.values()) else 'hi')
                for x in module.outputs:
                    q.append((module.name, x, outgoing))


first_round(modules, broadcast_targets)
second_round(modules, broadcast_targets)
