import re

PATTERN = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'


def to_int(val: str) -> int:
    if val.isdigit():
        return int(val)
    else:
        match val:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9


def get_calibration_sum(input_lines):
    lines = input_lines.split("\n")
    result = []
    for line in lines:
        if len(line):
            found_digits = re.findall(PATTERN, line)
            result.append(to_calibration_value(found_digits[0], found_digits[len(found_digits) - 1]))

    return sum(result)


def to_calibration_value(first_digit: str, last_digit: str) -> int:
    return to_int(first_digit) * 10 + to_int(last_digit)


def main():
    with open('input/day1.txt', 'r') as f:
        return get_calibration_sum(f.read())


def test_day1():
    input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
    expected = sum([12, 38, 15, 77])
    actual = get_calibration_sum(input)
    assert expected == actual


def test_day1_star2():
    input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
    expected = sum([29, 83, 13, 24, 42, 14, 76])
    actual = get_calibration_sum(input)
    assert expected == actual
