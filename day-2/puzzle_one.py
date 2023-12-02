import re
from re import Pattern

GAME_PATTERN = re.compile(r'^Game (?P<game_no>\d+): (?P<game_info>.*)$')
RED_PATTERN = re.compile(r'(?P<count>\d+)\sred')
GREEN_PATTERN = re.compile(r'(?P<count>\d+)\sgreen')
BLUE_PATTERN = re.compile(r'(?P<count>\d+)\sblue')
MAX = {'red': 12, 'green': 13, 'blue': 14}


def solve(lines: list[str]):
    _sum = 0
    for line in lines:
        match = GAME_PATTERN.match(line)
        game_no = int(match.group('game_no'))
        possible = determine_possible(match.group('game_info'))

        if possible:
            _sum += game_no

    return _sum


def determine_possible(game_info: str) -> bool:
    game_info = split_game_info(game_info)
    for red, green, blue in game_info:
        if red > MAX.get('red') or green > MAX.get('green') or blue > MAX.get('blue'):
            return False

    return True


def split_game_info(game_info: str) -> list[(int, int, int)]:
    rolls = game_info.split('; ')
    return [(
        find_color(roll, RED_PATTERN),
        find_color(roll, GREEN_PATTERN),
        find_color(roll, BLUE_PATTERN)
    ) for roll in rolls]


def find_color(roll: str, pattern: Pattern) -> int:
    match = pattern.search(roll)
    return int(match.group('count')) if match else 0
