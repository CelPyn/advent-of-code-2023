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
            dest, src, dist = (int(num) for num in line.split())
            maps[-1].append((src, dest, dist))

    for _map in maps:
        _map.sort()

    return seeds, maps


def solve(lines: list[str]) -> int:
    seeds, maps = parse(lines)
    lowest_locations = []

    for start, length in zip(*[iter(seeds)] * 2):
        src_ranges = [(start, start + length - 1)]
        dst_ranges = []

        for mapping in maps:
            for lo, hi in src_ranges:
                for src, dest, dist in mapping:

                    # entire source range is less than any mapping
                    # pass through source range as destination range
                    if hi < src:
                        dst_ranges.append((lo, hi))
                        break

                    # source range is contained within this range
                    elif lo >= src and lo < src + dist:

                        # the end of the source range is past this range
                        # add a destination range for the part within this range
                        # and continue processing the rest of the source range
                        if hi >= src + dist:
                            dst_ranges.append((dest + (lo - src), dest + dist - 1))
                            lo = src + dist

                        # the source range is wholly contained within this range
                        # map the entire range as the destination range
                        else:
                            dst_ranges.append((dest + (lo - src), dest + (hi - src)))
                            break

                    # part of the source range is less than any mapping
                    # add a destination range passing through the part not in a mapping
                    # and continue processing for the rest of the source range
                    elif lo < src and hi >= src:
                        dst_ranges.append((lo, src - 1))
                        lo = src

                # the source range was not contained within any mapping
                # pass through the source range as the destination range
                else:
                    dst_ranges.append((lo, hi))

            # results of one mapping become the ranges for the next
            src_ranges = dst_ranges
            dst_ranges = []

        # find the lowest result out of all the final ranges
        lowest_locations.append(min(lo for lo, _ in src_ranges))

    return min(lowest_locations)
