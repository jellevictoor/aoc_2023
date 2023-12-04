from functions import clean_lines


def has_neighbour(schematic_lines, x, y):
    for _y in [y - 1, y, y + 1]:
        if 0 <= _y < len(schematic_lines):
            for _x in [x - 1, x, x + 1]:
                if 0 <= _x < len(schematic_lines[_y]):
                    print(f"checking {y} and {x} for {_y},{_x}")
                    neighbour = schematic_lines[_y][_x]
                    if not (neighbour.isdigit() or neighbour == '.'):
                        return [{'symbol': neighbour}]
    return []


def get_neighbour(schematic_lines, col, row):
    for _row in [row - 1, row, row + 1]:
        if 0 <= _row < len(schematic_lines):
            for _col in [col - 1, col, col + 1]:
                if 0 <= _col < len(schematic_lines[_row]):
                    print(f"checking {row} and {col} for {_row},{_col}")
                    neighbour = schematic_lines[_row][_col]
                    if not (neighbour.isdigit() or neighbour == '.'):
                        return [{'symbol': neighbour}]
    return []


def get_part_numbers(schematic_lines):
    rich_result = []
    for y, line in enumerate(schematic_lines):
        neighbour_part_numbers = []
        number = ''
        for x, symbol in enumerate(list(line)):
            if symbol.isdigit():
                number += symbol
                if len(neighbour_part_numbers) == 0:
                    neighbour_part_numbers += has_neighbour(schematic_lines, x, y)
            if not symbol.isdigit():
                if len(neighbour_part_numbers) > 0:
                    rich_result.append(int(number))
                    neighbour_part_numbers = []
                number = ''
        if len(neighbour_part_numbers) > 0:
            rich_result.append(int(number))
    return sum(rich_result)


def get_gear_ratio(schematic_lines):
    gear_ratio = []
    for row, line in enumerate(schematic_lines):
        for col, symbol in enumerate(list(schematic_lines[row])):
            if schematic_lines[row][col] == '*':
                has_neighbour()
    return sum(gear_ratio)


def main():
    with open('input/day3.txt', 'r') as f:
        return get_gear_ratio(clean_lines(f.read()))


def test_day3_star1():
    schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    expected = 4361
    actual = get_part_numbers(clean_lines(schematic))
    assert expected == actual


def test_day3_star1_first_3_lines():
    schematic = """..172..............................454..46.......507..........809......923.778..................793..............137.............238........
............*.........712........=.......*................515.*...........*.......690.........../..........658.........=.........*..........
.........823.835........%.........710.....749........134..%............................#812...&.....925.../..........276.......386..........
"""
    expected = sum([46, 809, 923, 778, 793, 238, 712, 515, 658, 823, 835, 710, 749, 812, 276, 386])
    actual = get_part_numbers(clean_lines(schematic))
    assert expected == actual


def test_day3_star1_last_3_lines():
    schematic = """....546......*....454...120..683.............923.....@...*...865.574......276........56......57.659..*................-...-...512...........
............329...*.................................606.599...................*927..*.........-.......674..*........723..974................
................378..911........987.....606......................899.73....489......848.....................664...............388......589..

"""
    expected = sum([454, 56, 57, 329, 606, 599, 927, 674, 723, 974, 378, 489, 848, 664])
    actual = get_part_numbers(clean_lines(schematic))
    assert expected == actual


def test_day3_start1_reddit_example():
    schematic = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78..........
.......23...
....90*12...
............
2.2......12.
.*.........*
1.1.......56"""
    actual = get_part_numbers(clean_lines(schematic))
    assert 413 == actual


def test_day3_star2():
    schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    actual = get_gear_ratio(clean_lines(schematic))
    assert 467835 == actual
