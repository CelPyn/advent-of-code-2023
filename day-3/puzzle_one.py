import re

NUM_PATTERN = re.compile(r'\d+')
SYMBOL_PATTERN = re.compile(r'[@#$%&*\-+=/]')


def solve(lines: list[str]) -> int:
    padding = '.' * len(lines[0])
    padded = [padding] + lines
    parts = []
    for index, line in enumerate(lines):
        for match in NUM_PATTERN.finditer(line):
            start, end = match.span()
            start, end = max(start - 1, 0), min(end + 1, len(line))
            region = ''.join([row[start:end] for row in padded[index:index + 3]])
            if SYMBOL_PATTERN.search(region):
                parts.append(int(match.group(0)))
    return sum(parts)
