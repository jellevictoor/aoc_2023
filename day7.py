from dataclasses import dataclass

from functions import clean_lines


@dataclass
class Hand:
    hand: list[str]
    bid: int
    score: int
    result_score = {
        'five_of_a_kind': 7,
        'four_of_a_kind': 6,
        'full_house': 5,
        'three_of_a_kind': 4,
        'two_pair': 3,
        'one_pair': 2,
        'high_card': 1
    }
    card_score = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.score = self._get_score()

    def __lt__(self, other):
        if self.score == other.score:
            for i in range(len(self.hand)):
                my_card_score_index = self.card_score.index(self.hand[i])
                other_card_index = self.card_score.index(other.hand[i])

                if my_card_score_index > other_card_index:
                    return True
                elif other_card_index > my_card_score_index:
                    return False
        return self.score < other.score

    def __repr__(self):
        return f"{self.hand} = {self.score}"

    def _get_score(self):
        grouped = {c: self.hand.count(c) for c in set(self.hand) if c != 'J'}
        card_count = {value: key for key, value in grouped.items()}
        joker_count = self.hand.count('J')
        if len(grouped) <= 1:
            score = self.result_score['five_of_a_kind']
        elif len(grouped) == 2:
            if (4 - joker_count) in card_count:
                score = self.result_score['four_of_a_kind']
            else:
                score = self.result_score['full_house']
        elif len(grouped) == 3:
            if (3 - joker_count) in card_count:
                score = self.result_score['three_of_a_kind']
            else:
                score = self.result_score['two_pair']
        elif len(grouped) == 4:
            score = self.result_score['one_pair']
        else:
            score = self.result_score['high_card']
        return score


def solve(lines):
    hands = [Hand(list(line.split(' ')[0]), int(line.split(' ')[1])) for line in lines]
    sorted_hands = sorted(hands)
    scores = []
    for i, hand in enumerate(sorted_hands):
        scores.append(hand.bid * (i + 1))
    return sum(scores)


def main():
    with open('input/day7.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day7_star1():
    input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
    expected = 5905
    actual = solve(clean_lines(input))
    assert actual == expected


def test_day7_small():
    assert Hand("JJJJJ", 1).score == 7
    assert Hand("J68JJ", 1).score == 6
    assert Hand("23332", 1).score == 5
    assert Hand("TTT98", 1).score == 4
    assert Hand("23432", 1).score == 3
    assert Hand("A23A4", 1).score == 2
    assert Hand("23456", 1).score == 1
