from functions import clean_lines


def has_neighbour(schematic_lines, x, y):
    for _y in [y - 1, y, y + 1]:
        if 0 <= _y < len(schematic_lines):
            for _x in [x - 1, x, x + 1]:
                if 0 <= _x < len(schematic_lines[_y]):
                    print(f"checking {y} and {x} for {_y},{_x}")
                    neighbour = schematic_lines[_y][_x]
                    if not (neighbour.isdigit() or neighbour == '.'):
                        return True
    return False


def get_part_numbers(schematic_lines):
    rich_result = []
    for y, line in enumerate(schematic_lines):
        is_part_number = False
        number = ''
        for x, symbol in enumerate(list(line)):
            if symbol.isdigit():
                number += symbol
                if not is_part_number:
                    is_part_number = has_neighbour(schematic_lines, x, y)
            if not symbol.isdigit():
                if is_part_number:
                    rich_result.append(int(number))
                    is_part_number = False
                number = ''
        if is_part_number:
            rich_result.append(int(number))
    return sum(rich_result)


def main():
    with open('input/day3.txt', 'r') as f:
        return get_part_numbers(clean_lines(f.read()))


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
