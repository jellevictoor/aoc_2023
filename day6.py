import re

from functions import clean_lines


def solve(lines):
    time = [int(time) for time in re.findall(r'\d+', lines[0])]
    distance = [int(distance) for distance in re.findall(r'\d+', lines[1])]
    for index in range(len(time)):
        print(f"race {index+1}, time: {time[index]}, distance: {distance[index]}")


def main():
    with open('input/day6.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day6_star1():
    input = """
Time:      7  15   30
Distance:  9  40  200
"""
    expected = 288
    actual = solve(clean_lines(input))
    assert actual == expected
