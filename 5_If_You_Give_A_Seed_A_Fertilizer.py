import heapq


def read_input() -> tuple[list[str], dict[str: list[list[int]]]]:

    MAPS: set(str) = (
        'seed-to-soil map:', 'soil-to-fertilizer map:',
        'fertilizer-to-water map:', 'water-to-light map:',
        'light-to-temperature map:',  'temperature-to-humidity map:',
        'humidity-to-location map:'
    )

    with open('Advent_of_code_2023/data/input_day_5.txt', 'r') as file:

        seeds: list[str] = list(map(int,
                                    file.readline().lstrip('seeds:').split()))
        map_of_maps: list[list[list[int]]] = [[] for _ in range(7)]
        index: int = 0

        for line in file:
            line = line.rstrip('\n')
            if line in MAPS:
                while line:
                    line = file.readline().rstrip('\n').split()
                    if line:
                        map_of_maps[index].append(list(map(int, line)))
                index += 1

        return (seeds, map_of_maps)


# Part one
def dijkstra(seed: int, map_of_maps: list[list[list[int]]]) -> int:

    queue: list[tuple[int, int]] = [(seed, -1)]
    heapq.heapify(queue)

    while queue:
        dummy_seed, start_map = heapq.heappop(queue)
        flag: bool = False

        if start_map+1 == 7:
            seed = min(seed, dummy_seed)
            continue

        for small_map in map_of_maps[start_map+1]:
            if small_map[1] <= dummy_seed:
                dif = dummy_seed-small_map[1]
                if dif <= small_map[2]:
                    heapq.heappush(queue, (small_map[0]+dif, start_map+1))
                    flag = True
        if not flag:
            heapq.heappush(queue, (dummy_seed, start_map+1))

    return seed


# Part two
def mapping_range(seed: tuple[int, int],
                  map_of_maps: list[list[list[int]]]) -> tuple[int,
                                                               int] | None:
    global seeds

    new: list[tuple[int, int, int]] = [seed]

    while new:

        seed_start, seed_end, start_map = new.pop()

        if start_map+1 == 7:
            continue

        for small_map in map_of_maps[start_map+1]:
            destination, source, lenght = small_map
            # Borders of intersection
            start_inter = max(seed_start, source)
            end_inter = min(seed_end, source + lenght)

            if start_inter < end_inter:
                new.append((start_inter - source + destination,
                           end_inter - source + destination, start_map+1))
                if start_inter > seed_start:
                    seeds.append((seed_start, start_inter, start_map))
                if seed_end > end_inter:
                    seeds.append((end_inter, seed_end, start_map))
                break
        else:
            new.append((seed_start, seed_end, start_map+1))

    return (seed_start, seed_end)


seeds, map_of_maps = read_input()

# part one
# for i, seed in enumerate(seeds):
#     seeds[i] = dijkstra(seed, map_of_maps)
# print(min(seeds))

# Part two PIZDA
result: set[int] = set()
seeds: list[tuple[int, int, int]] = [(seeds[i-1], seeds[i-1]+seeds[i], -1)
                                     for i in range(1, len(seeds), 2)]

while seeds:
    result.add(mapping_range(seeds.pop(), map_of_maps))

print(min(result)[0])
