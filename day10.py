from dataclasses import dataclass
from typing import List

from functions import clean_lines

WEST_VALUES = ('S', '-', 'L', 'F')
EAST_VALUES = ('S', '-', '7', 'J')

NORTH_VALUES = ('S', '|', 'F', '7')
SOUTH_VALUES = ('S', '|', 'L', 'J')


@dataclass
class Position:
    row: int
    col: int
    value: str

    def __init__(self, row, col, grid):
        self.row = row
        self.col = col
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
            self.value = grid[row][col]
        else:
            self.value = '.'


@dataclass
class Map:
    grid: List[List[str]]

    def get_neighbours(self, position):
        north = Position(position.row - 1, position.col, self.grid)
        east = Position(position.row, position.col + 1, self.grid)
        south = Position(position.row + 1, position.col, self.grid)
        west = Position(position.row, position.col - 1, self.grid)
        return north, east, south, west

    def get_starting_position(self):
        return [Position(row_num, col_num, self.grid)
                for row_num, row in enumerate(self.grid)
                for col_num, field in enumerate(row) if field == 'S'][0]

    def get_steps(self):
        starting_position = self.get_starting_position()
        direction = ''
        current_position = starting_position
        steps = []
        while current_position != starting_position or len(steps) == 0:
            neighbours = self.get_neighbours(current_position)
            # | is a vertical pipe connecting north and south.
            # - is a horizontal pipe connecting east and west.
            # L is a 90-degree bend connecting north and east.
            # J is a 90-degree bend connecting north and west.
            # 7 is a 90-degree bend connecting south and west.
            # F is a 90-degree bend connecting south and east.
            if direction != 'SOUTH' and neighbours[0].value in NORTH_VALUES:
                direction = 'NORTH'
                current_position = self.get_position(current_position.row - 1, current_position.col)
            elif direction != 'NORTH' and neighbours[2].value in SOUTH_VALUES:
                direction = 'SOUTH'
                current_position = self.get_position(current_position.row + 1, current_position.col)
            elif direction != 'EAST' and neighbours[3].value in WEST_VALUES:
                direction = 'WEST'
                current_position = self.get_position(current_position.row, current_position.col - 1)
            elif direction != 'WEST' and neighbours[1].value in EAST_VALUES:
                direction = 'EAST'
                current_position = self.get_position(current_position.row, current_position.col + 1)
            else:
                raise Exception(f'stuck on {current_position}, coming from {direction} in {steps} steps.')
            steps.append(current_position)
        return steps

    def get_position(self, row, col):
        return Position(row, col, self.grid)


def solve(lines):
    return len(Map(lines).get_steps()) / 2


def main():
    with open('input/day10.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day10_star1_simple():
    input = """.....
.S-7.
.|.|.
.L-J.
.....
"""
    expected = 4
    actual = solve(clean_lines(input))
    assert actual == expected


def test_day10_star1_complex():
    input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
    expected = 8
    actual = solve(clean_lines(input))
    assert actual == expected
