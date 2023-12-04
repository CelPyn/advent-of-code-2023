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

        winning_count = 0
        for n in actual:
            if n in winning:
                winning_count += 1

        if winning_count == 1:
            points.append(1)
        elif winning_count > 0:
            points.append(int(math.pow(2, winning_count - 1)))

    return sum(points)
