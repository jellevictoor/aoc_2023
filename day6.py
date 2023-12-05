
from functions import clean_lines

def solve(lines):
    ...


def main():
    with open('input/day6.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day6_star1():
    input = """\
"""
    expected = 35
    actual = solve(clean_lines(input))
    assert actual == expected
