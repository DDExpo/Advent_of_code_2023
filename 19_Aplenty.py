from pprint import pprint
from time_exucute import time_excution


def read_input() -> tuple[dict[str: dict[str]], list[dict[str: str]]]:
    with open('Advent_of_code_2023/data/test.txt') as file:

        workflows = {}
        parts: list[str] = []
        for line in file:
            if line == '\n':
                break
            key, line = line.rstrip('}\n').split('{')
            workflows[key] = line.split(',')

        for line in file:
            line = line.lstrip('{').rstrip('}\n').split(',')
            parts.append({li[0]: int(li[2:]) for li in line})

    return (workflows, parts)


@time_excution
def first_round(workflows: dict[str: list[str]],
                parts: list[dict[str: int]], start: str):

    total: int = 0
    opt: dict[str: int] = {'>': int.__gt__,
                           '<': int.__le__}

    for part in parts:
        queue = [start]
        while queue:
            cur_workflows = workflows[queue.pop()]
            for workflow in cur_workflows:
                if workflow == 'A':
                    total += sum(map(int, part.values()))
                    break
                elif workflow == 'R':
                    break

                if 1 < len(workflow) <= 3:
                    queue.append(workflow)
                    break

                workflow, if_workflow = workflow.split(':')
                key = workflow[0]
                num = int(workflow[2:])

                if opt[workflow[1]](part[key], num):
                    if if_workflow == 'A':
                        total += sum(map(int, part.values()))
                        break
                    elif if_workflow == 'R':
                        break
                    else:
                        queue.append(if_workflow)
                        break
                else:
                    continue

    print(total)


def second_round(workflows: list[dict[str: int]]):

    xmas: dict[set[int]] = {k: set() for k in 'xmas'}
    total: int = 1

    workflows = workflows.values()
    pprint(sorted(workflows, key=lambda x: x[0]), compact=True, width=156)
    for workflow in workflows:
        workflow, fallback = workflow, workflow.pop()
        for work in workflow:

            equ, if_equ = work.split(':')
            if equ[1] == '>':

                if if_equ == 'A' and fallback == 'A':
                    xmas[equ[0]].add('-'+equ[2:])
                elif if_equ == 'A':
                    xmas[equ[0]].add('+'+equ[2:])
                elif if_equ == 'R':
                    xmas[equ[0]].add('-'+equ[2:])
                else:
                    if fallback == 'A':
                        xmas[equ[0]].add('+'+equ[2:])

            elif equ[1] == '<':

                if if_equ == 'A' and fallback == 'A':
                    xmas[equ[0]].add('+'+equ[2:])
                elif if_equ == 'A':
                    xmas[equ[0]].add('-'+equ[2:])
                elif if_equ == 'R':
                    xmas[equ[0]].add('+'+equ[2:])
                else:
                    if fallback == 'A':
                        xmas[equ[0]].add('+'+equ[2:])

    for rxmas in xmas.values():

        rxmas = sorted(rxmas, key=lambda x: int(x[1:]))
        rxmas.append('-4000')
        rxmas.insert(0, '+1')
        pprint(rxmas, compact=True, width=156)
        if rxmas[-1][0] == '+':
            rxmas.append('-4000')
        last_rang = 0
        total_range = 0
        for i in range(1, len(rxmas)):
            cur, prev = rxmas[i], rxmas[i-1]
            cur_symb, cur_num = cur[0], int(cur[1:])
            prev_symb, prev_num = prev[0], int(prev[1:])
            if cur_symb == '+' and prev_symb == '-':
                total_range += abs(prev_num - last_rang - 1)
                last_rang = cur_num

            elif cur_symb == '-' and prev_symb == '+':
                total_range += abs(cur_num - last_rang - 1)
                last_rang = cur_num

        print(total_range)
        total *= total_range
    print(total)


workflows, parts = read_input()
first_round(workflows, parts, 'in')
second_round(workflows)
