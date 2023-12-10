import math
import re

from functions import clean_lines


def solve(lines):
    instructions = list(lines[0])
    regex = r'[A-Z]{3}'
    graph = {re.findall(regex, s)[0]: (re.findall(regex, s)[1], re.findall(regex, s)[2]) for s in lines[1:]}
    start_positions = [key for key in graph.keys() if key[2] == 'A']
    shortest_paths = []
    for position in start_positions:
        current_position = position
        steps = 0
        while current_position[2] != 'Z':
            for instruction in instructions:

                if instruction == 'L':
                    current_position = graph[current_position][0]
                else:
                    current_position = graph[current_position][1]
                steps += 1
                if current_position[2] == 'Z':
                    break
        shortest_paths.append(steps)
    return math.lcm(*shortest_paths)


def main():
    with open('input/day8.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day8_star1_small():
    input = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

"""
    expected = 2
    actual = solve(clean_lines(input))
    assert actual == expected


def test_day8_star1():
    input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

"""
    expected = 6
    actual = solve(clean_lines(input))
    assert actual == expected
