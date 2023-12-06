import puzzle_one
import puzzle_two
import datetime


def read_input(path):
    with open(path, 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    lines = read_input("inputs/one.txt")
    start = datetime.datetime.now()
    result = puzzle_two.solve(lines)
    end = datetime.datetime.now()
    delta = end - start
    print(f'Result: {result}')
    print(f'Delta: {delta} - Microseconds: {delta.microseconds}')
