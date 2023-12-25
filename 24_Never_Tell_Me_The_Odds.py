import sympy


# Part one
class Hailstones:

    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

    def __repr__(self) -> str:
        return 'Hailstone{' + f'a={self.a}, b={self.b}, c={self.c}' + '}'


hailstones: list[list[int]] = [
    Hailstones(*map(int, line.replace('@', ',').split(',')))
    for line in open('Advent_of_code_2023/data/input_day_24.txt'
                     ).read().splitlines()
]

total: int = 0

for i, hs1 in enumerate(hailstones):
    for hs2 in hailstones[:i]:
        a1, b1, c1 = hs1.a, hs1.b, hs1.c
        a2, b2, c2 = hs2.a, hs2.b, hs2.c
        if a1*b2 == b1*a2:
            continue
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if 2*10**14 <= x <= 4*10**14 and 2*10**14 <= y <= 4*10**14:
            if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0
                    for hs in (hs1, hs2)):
                total += 1

print(total)


# math method slow for me
hailstones: list[list[int]] = [
    tuple(map(int, line.replace('@', ',').split(',')))
    for line in open('Advent_of_code_2023/data/input_day_24.txt'
                     ).read().splitlines()
]

total_math: int = 0

for i, hs1 in enumerate(hailstones):
    for hs2 in hailstones[:i]:
        px, py = sympy.symbols('px py')
        answers = sympy.solve([vy * (px - sx) - vx * (py - sy) for
                               sx, sy, _, vx, vy, _ in [hs1, hs2]])
        if answers == []:
            continue
        x, y = answers[px], answers[py]
        if 2*10**14 <= x <= 4*10**14 and 2*10**14 <= y <= 4*10**14:
            if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0
                   for sx, sy, _, vx, vy, _ in [hs1, hs2]):
                total_math += 1

print(total_math)


# Part two
equations = []
xr, yr, zr, vxr, vyr, vzr = sympy.symbols('xr, yr, zr, vxr, vyr, vzr')

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))

    if i < 2:
        continue

    answers = [soln for soln in sympy.solve(equations)
               if all(x % 1 == 0 for x in soln.values())]
    if len(answers) == 1:
        break

answers = answers[0]
print(i)
print(answers[xr] + answers[yr] + answers[zr])
