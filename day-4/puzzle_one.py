import math
import re

NUM_PATTERN = re.compile(r'\d+')


def solve(lines: list[str]) -> int:
    points = []
    for line in lines:
        split = line.split('|')
        winning = split[0].split(':')[1]
        winning = set([winning[match.start():match.end()] for match in NUM_PATTERN.finditer(winning)])
        actual = [split[1][match.start():match.end()] for match in NUM_PATTERN.finditer(split[1])]

        win_count = sum([1 for n in actual if n in winning])

        if win_count == 1:
            points.append(1)
        elif win_count > 0:
            points.append(int(math.pow(2, win_count - 1)))

    return sum(points)
