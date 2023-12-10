import re
from itertools import pairwise

from functions import clean_lines


def solve(lines):
    additions = []
    for line in lines:
        sequence = re.findall(r"-?\d+", line)
        sequence = [int(x) for x in sequence]
        result = sequence
        steps = [sequence]
        while not all([True if x == 0 else False for x in result]):
            result = [pair[1] - pair[0] for pair in pairwise(result)]
            steps.append(result)
        previous = 0
        steps.reverse()
        for step in steps:
            if len(step):
                last_element = step[0]
                step.insert(0, last_element-previous)
                previous = step[0]
        additions.append(steps[-1][0])
    return sum(additions)


def main():
    with open('input/day9.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day9_star1_small():
    input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
    expected = 2
    actual = solve(clean_lines(input))
    assert actual == expected
def test_day9_star2_small():
    input = """10 13 16 21 30 45"""
    expected = 5
    actual = solve(clean_lines(input))
    assert actual == expected



def test_day9_star1_smaller():
    input = """0 -1 2"""

    # -1 - 3 (7)
    # 4 (4)
    # 0
    expected = 9
    actual = solve(clean_lines(input))
    assert actual == expected
