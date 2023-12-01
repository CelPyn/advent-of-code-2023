import re

mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solve(lines: list[str]) -> int:
    _sum = 0
    for line in lines:
        nums_in_line = [s for s in re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)]

        first = to_intstr(nums_in_line[0])
        last = to_intstr(nums_in_line[-1])

        result = first + last
        _sum += int(result)
    return _sum


def to_intstr(val) -> str:
    return mapping.get(val, val)
