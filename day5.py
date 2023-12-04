from functions import clean_lines


def solve(input):
    pass


def main():
    with open('input/day5.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day5_star1():
    input = """"""
    expected = -1
    actual = solve(clean_lines(input))
    assert expected == actual
