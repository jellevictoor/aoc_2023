import re


def to_str(val: str) -> str:
    if val.isdigit():
        return val
    else:
        result = ""
        match val:
            case "one":
                result = 1
            case "two":
                result = 2
            case "three":
                result = 3
            case "four":
                result = 4
            case "five":
                result = 5
            case "six":
                result = 6
            case "seven":
                result = 7
            case "eight":
                result = 8
            case "nine":
                result = 9

        return str(result)


def solve(input_lines):
    lines = input_lines.split("\n")
    result = []
    for line in lines:
        if len(line) > 0:
            first = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            result.append(int(to_str(first[0]) + to_str(first[len(first) - 1])))

    return sum(result)


def main():
    with open('input/day1.txt', 'r') as f:
        result = solve(f.read())
        # 53846 is too low
        return result


def test_day1():
    input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
    expected = sum([12, 38, 15, 77])
    actual = solve(input)
    assert expected == actual


def test_day1_star2():
    input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
evsevenef
one
two
three
four
five
six
seven
eight
nine
"""
    expected = sum([29, 83, 13, 24, 42, 14, 76, 77, 11, 22, 33, 44, 55, 66, 77, 88, 99])
    actual = solve(input)
    assert expected == actual


def test_main():
    print(main())
