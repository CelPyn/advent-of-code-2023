import re

NUM_PATTERN = re.compile(r'\d+')


def solve(lines: list[str]) -> int:
    cards = [0] * len(lines)
    for index, line in enumerate(lines):
        cards[index] += 1
        split = line.split('|')
        winning = split[0].split(':')[1]
        winning = set([winning[match.start():match.end()] for match in NUM_PATTERN.finditer(winning)])
        actual = [split[1][match.start():match.end()] for match in NUM_PATTERN.finditer(split[1])]

        win_count = sum([1 for n in actual if n in winning])
        for i in range(1, win_count + 1):
            cards[index + i] += (1 * cards[index])

    return sum(cards)
