import re


def solve(lines: list[str]):
    _sum = 0
    for line in lines:
        nums_in_line = [s for s in re.findall(r'(\d)', line)]
        print(nums_in_line)

        first = nums_in_line[0]
        last = nums_in_line[-1]

        result = first + last
        _sum += int(result)
    print(_sum)
