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

    def can_go_north(self):
        return self.value in SOUTH_VALUES

    def can_go_south(self):
        return self.value in NORTH_VALUES

    def can_go_east(self):
        return self.value in WEST_VALUES

    def can_go_west(self):
        return self.value in EAST_VALUES


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
            if direction != 'SOUTH' and current_position.can_go_north() and neighbours[0].value in NORTH_VALUES:
                direction = 'NORTH'
                current_position = self.get_position(current_position.row - 1, current_position.col)
            elif direction != 'NORTH' and current_position.can_go_south() and neighbours[2].value in SOUTH_VALUES:
                direction = 'SOUTH'
                current_position = self.get_position(current_position.row + 1, current_position.col)
            elif direction != 'EAST' and current_position.can_go_west() and neighbours[3].value in WEST_VALUES:
                direction = 'WEST'
                current_position = self.get_position(current_position.row, current_position.col - 1)
            elif direction != 'WEST' and current_position.can_go_east() and neighbours[1].value in EAST_VALUES:
                direction = 'EAST'
                current_position = self.get_position(current_position.row, current_position.col + 1)
            else:
                raise Exception(f'stuck on {current_position}, coming from {direction} in {steps} steps.')
            steps.append(current_position)
        return steps

    def get_position(self, row, col):
        return Position(row, col, self.grid)

    def visualize_map(self):
        print()
        for row in self.grid:
            visual_row = ''
            for tile in row:
                if tile == '.':
                    visual_row += ' . '  # Space added for readability
                elif tile == 'O':
                    visual_row += ' O '  # Flood-filled area
                elif tile == 'P':
                    visual_row += ' P '  # Path
                elif tile == '|':
                    visual_row += ' │ '  # Vertical pipe
                elif tile == '-':
                    visual_row += ' ─ '  # Horizontal pipe
                elif tile == 'L':
                    visual_row += ' └ '  # Corner
                elif tile == 'J':
                    visual_row += ' ┘ '  # Corner
                elif tile == '7':
                    visual_row += ' ┐ '  # Corner
                elif tile == 'F':
                    visual_row += ' ┌ '  # Corner
                else:
                    visual_row += f' {tile} '  # Other characters
            print(visual_row)
        print()

    def mark_positions(self, steps, marker):
        for step in steps:
            self.grid[step.row][step.col] = marker


    def flood_fill(self, row, col, target, replacement):
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[row]):
            return
        if self.grid[row][col] != target:
            return

        self.grid[row][col] = replacement

        for d_row, d_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            self.flood_fill(row + d_row, col + d_col, target, replacement)

    def run_edge_flood_fill(self, target, replacement):
        for row in range(len(self.grid)):
            self.flood_fill(row, 0, target, replacement)  # Left edge
            self.flood_fill(row, len(self.grid[row]) - 1, target, replacement)  # Right edge
        for col in range(len(self.grid[0])):
            self.flood_fill(0, col, target, replacement)  # Top edge
            self.flood_fill(len(self.grid) - 1, col, target, replacement)  # Bottom edge

    def count_enclosed_tiles(self):
        # Find the loop using your existing method
        loop_positions = self.get_steps()

        # Create an empty map with the loop drawn on it
        self.grid = empty_map = [['.' for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]

        for position in loop_positions:
            empty_map[position.row][position.col] = '#'  # Use 'L' to represent the loop

        # Perform a flood-fill from the edges to mark the outside area
        self.run_edge_flood_fill('.', 'O')

        # Count the remaining tiles within the loop that are not part of the outside area
        enclosed_count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if not empty_map[row][col] == '#' and self.grid[row][col] != 'O':
                    enclosed_count += 1
        self.visualize_map()
        return enclosed_count


def solve(lines):
    map = get_map(lines)
    return map.count_enclosed_tiles()

def find_loop(lines):
    return len(get_map(lines).get_steps()) / 2


def get_map(lines):
    return Map([list(line) for line in lines])


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
    actual = find_loop(clean_lines(input))
    assert actual == expected


def test_day10_star1_complex():
    input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
    expected = 8
    actual = find_loop(clean_lines(input))
    assert actual == expected


def test_day10_find_simple_enclosed():
    input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
    expected = 4
    actual = solve(clean_lines(input))
    assert actual == expected


def test_day10_find_loop_complex():
    input = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""
    expected = 8
    actual = solve(clean_lines(input))
    assert actual == expected

def test_day10_find_loop_loose_parts():
    input = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
    expected = 10
    actual = solve(clean_lines(input))
    assert actual == expected
