import re
from re import Pattern

GAME_PATTERN = re.compile(r'^Game (?P<game_no>\d+): (?P<game_info>.*)$')
RED_PATTERN = re.compile(r'(?P<count>\d+)\sred')
GREEN_PATTERN = re.compile(r'(?P<count>\d+)\sgreen')
BLUE_PATTERN = re.compile(r'(?P<count>\d+)\sblue')


def solve(lines: list[str]):
    _sum = 0
    for line in lines:
        match = GAME_PATTERN.match(line)
        min_power = determine_minimum_power(match.group('game_info'))

        _sum += min_power

    return _sum


def determine_minimum_power(game_info: str) -> int:
    game_info = split_game_info(game_info)
    max_red = 0
    max_green = 0
    max_blue = 0
    for red, green, blue in game_info:
        if red > max_red:
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue

    return max_red * max_green * max_blue


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
