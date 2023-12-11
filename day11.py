import itertools
from dataclasses import dataclass
from typing import List

from functions import clean_lines


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

    def __lt__(self, other):
        return self.col + self.row < other.col + other.row

    def __hash__(self):
        return self.value.__hash__() + self.col.__hash__() + self.row.__hash__()


def manhattan(a, b):
    return abs(a.col - b.col) + abs(a.row - b.row)


@dataclass
class Combo:
    start: Position
    stop: Position

    def __init__(self, start, stop):
        if start.col + start.row < stop.col + stop.row:
            self.start = start
            self.stop = stop
        else:
            self.stop = start
            self.start = stop

    def __hash__(self):
        return self.start.__hash__() + self.stop.__hash__()

    def __lt__(self, other):
        if self.start.col < other.start.col:
            return self.start.col < other.start.col
        return self.start.row < other.start.row


@dataclass
class Map:
    grid: List[List[str]]

    def __init__(self, grid):
        self.grid = grid
        self.empty_rows, self.empty_columns = self.get_empty_rows_and_columns()

    def get_empty_rows_and_columns(self):
        empty_rows = []
        empty_columns = []
        for row in range(len(self.grid)):
            if self.grid[row].count('#') == 0:
                empty_rows.append(row)
        for col in range(len(self.grid[0])):
            full_column = ''
            for row in self.grid:
                full_column += row[col]
            if full_column.count('#') == 0:
                empty_columns.append(col)
        return empty_rows, empty_columns

    def get_galaxies(self) -> List[Position]:
        return [Position(row_num, col_num, self.grid)
                for row_num, row in enumerate(self.grid)
                for col_num, field in enumerate(row) if field == '#']

    def get_steps(self):
        galaxies = self.get_galaxies()
        combos = [Combo(c[0], c[1]) for c in itertools.combinations(galaxies, 2)]
        steps = []
        for combo in combos:
            distance = manhattan(combo.start, combo.stop)
            expansion = self.get_expansion(combo.start, combo.stop)
            steps.append(distance + expansion)
        return steps

    def get_position(self, row, col):
        return Position(row, col, self.grid)

    def _should_expand(self, start):
        return start.row in self.empty_rows or start.col in self.empty_columns

    def get_expansion(self, start, stop):
        row_traverse = range(min(start.row, stop.row), max(start.row, stop.row))
        col_traverse = range(min(start.col, stop.col), max(start.col, stop.col))
        empty_rows = len([row for row in row_traverse if row in self.empty_rows])
        empty_columns = len([col for col in col_traverse if col in self.empty_columns])
        return (empty_rows + empty_columns) * (1_000_000 - 1)


def solve(lines):
    steps = Map(lines).get_steps()
    return sum(steps)


def main():
    with open('input/day11.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day11_star1():
    input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    expected = 374
    actual = solve(clean_lines(input))
    assert actual == expected
