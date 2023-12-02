from functions import clean_lines


class Game:
    def __init__(self, id: int, rolls: list[dict]):
        self._id = id
        self._rolls = rolls

    def get_id(self):
        return self._id

    def is_valid(self, max):
        for roll in self._rolls:
            for key in roll:
                if roll[key] > max[key]:
                    return False
        return True

    def get_power(self):
        min_cubes = {}
        for roll in self._rolls:
            for key in roll:
                min_cubes[key] = max(min_cubes.get(key, 0), roll[key])
        power = 1
        for key in min_cubes:
            power *= min_cubes[key]
        return power


def solve_part_1(game_data, max_rolls):
    games = parse_games(game_data)
    result = []
    for game in games:
        if game.is_valid(max_rolls):
            result.append(game.get_id())

    return sum(result)


def parse_games(input):
    games = []
    for line in clean_lines(input):
        game_id, game_result = line.replace('Game ', '').split(':')
        results = game_result.strip().split('; ')
        rolls = []
        for roll in results:
            r = {}
            split = roll.split(', ')
            for pull in split:
                times, color = pull.split(' ')
                r[color] = int(times)
            rolls.append(r)
        games.append(Game(int(game_id), rolls))
    return games


def main():
    with open('input/day2.txt', 'r') as f:
        return solve_part_2(f.read())


def test_example_star_1():
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    expected = sum([1, 2, 5])
    actual = solve_part_1(input, {
        'red': 12,
        'green': 13,
        'blue': 14
    })
    assert expected == actual


def solve_part_2(input) -> int:
    games = parse_games(input)
    result = 0
    for game in games:
        result += game.get_power()
    return result


def test_example_star_2():
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    expected = sum([48, 12, 1560, 630, 36])
    actual = solve_part_2(input)
    assert expected == actual
