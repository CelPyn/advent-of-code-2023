import re

NUM_PATTERN = re.compile(r'\d+')
GEAR_PATTERN = re.compile(r'\*')


def solve(lines: list[str]) -> int:
    padding = '.' * len(lines[0])
    padded = [padding] + lines
    gear_ratios = []
    for index, line in enumerate(lines):
        for gear in GEAR_PATTERN.finditer(line):
            numbers = []
            for subset in padded[index:index+3]:
                for n in NUM_PATTERN.finditer(subset):
                    start, end = n.span()
                    if start - 1 <= gear.start() <= end:
                        numbers.append(int(n.group(0)))
            if len(numbers) == 2:
                gear_ratios.append(numbers[0] * numbers[1])
    return sum(gear_ratios)
