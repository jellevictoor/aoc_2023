import re

from functions import clean_lines


class Game:

    def __init__(self, game_id, winning_numbers, your_numbers):
        self._game_id = game_id
        self._winning_numbers = sorted(winning_numbers)
        self._your_numbers = sorted(your_numbers)

    def get_score(self):
        found_numbers = self.get_winning_numbers()
        score = 0
        if len(found_numbers):
            if len(found_numbers) == 1:
                score = 1
            else:
                score = pow(2, len(found_numbers) - 1)
        print(f"game {self._game_id} has score {score}")
        return score

    def get_winning_numbers(self):
        return [i for i in self._winning_numbers if i in self._your_numbers]

    def __str__(self):
        return f"game {self._game_id}"


def count_score(cards):
    games = [create_game(card) for card in cards]
    return sum([game.get_score() for game in games])


def get_copies(cards):
    games = [create_game(card) for card in cards]
    count_games = [{'game': game, 'count': 1} for index, game in enumerate(games)]
    for game in games:
        numbers = game.get_winning_numbers()
        for i in range(1, len(numbers) + 1):
            count_games[game._game_id - 1 + i]['count'] += count_games[game._game_id - 1]['count']

    return sum([game['count'] for game in count_games])


def create_game(card):
    game, card = card.split(':')
    game_id = game.replace('Card ', '')
    winning_numbers, your_numbers = card.split('|')
    return Game(int(game_id), re.findall(r"(\s?[\s|\d]?\d)", winning_numbers),
                re.findall(r"(\s?[\s|\d]?\d)", your_numbers))


def main():
    with open('input/day4.txt', 'r') as f:
        return get_copies(clean_lines(f.read()))


def test_day4_star1():
    input = """Card 1: 41 48 83 86 17  8 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
    expected = 13
    actual = count_score(clean_lines(input))
    assert expected == actual

def test_day4_star2():
    input = """Card 1: 41 48 83 86 17  8 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
    expected = 30
    actual = get_copies(clean_lines(input))
    assert expected == actual
