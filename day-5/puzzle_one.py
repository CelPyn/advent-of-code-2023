import re

NUM_PATTERN = re.compile(r'\d+')
MAP_LINE_PATTERN = re.compile(r'^.*map.*$')

Map = list[tuple[int, int, int]]


def parse(lines: list[str]) -> tuple[list[int], list[Map]]:
    seeds = [int(seed) for seed in NUM_PATTERN.findall(lines[0].split(':')[1])]
    maps: [Map] = []
    for line in lines[2:]:
        if MAP_LINE_PATTERN.match(line):
            maps.append([])
        elif line.strip():
            maps[-1].append(tuple(int(num) for num in NUM_PATTERN.findall(line)))

    for _map in maps:
        _map.sort()

    return seeds, maps


def solve(lines: list[str]) -> int:
    seeds, maps = parse(lines)
    locations: list[int] = []
    for seed in seeds:
        for _map in maps:
            for dest, src, length in _map:
                if seed in range(src, src + length + 1):
                    seed = dest + (seed - src)
                    break
        locations.append(seed)

    return min(locations)
