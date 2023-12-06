import re
from dataclasses import dataclass
from functools import reduce

from functions import clean_lines


@dataclass
class Race:
    race_no: int
    time: int
    distance: int


def solve(lines):
    time = int(''.join([time for time in re.findall(r'\d+', lines[0])]))
    distance = int(''.join([distance for distance in re.findall(r'\d+', lines[1])]))
    races = [Race(1,time,distance)]
    combos = []
    for race in races:
        print(f"race {race.race_no}, time: {race.time}, distance: {race.distance}")
        wins = 0
        for pressing_time in range(1, race.distance):
            if race.distance / pressing_time < (race.time - pressing_time):
                wins += 1
            elif wins > 0:
                break
        combos.append(wins)
    return reduce((lambda x, y: x * y), combos)


def main():
    with open('input/day6.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day6_star1():
    input = """
Time:      7  15   30
Distance:  9  40  200
"""
    expected = 71503
    actual = solve(clean_lines(input))
    assert actual == expected
