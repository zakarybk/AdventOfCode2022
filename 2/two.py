from pathlib import Path
from enum import IntEnum
from typing import List, Union


WIN_BONUS = 6
DRAW_BONUS = 3


class RPC:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Action:
    LOSE = 0
    DRAW = 1
    WIN = 2

    actions = {
        LOSE: {"x"},
        DRAW: {"y"},
        WIN: {"z"}
    }

    def __init__(self, action: str):
        self.action = next(
            rpc
            for rpc, vals in self.actions.items()
            if action.lower() in vals
        )


class Hand:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    hands = {
        ROCK: {"a"},
        PAPER: {"b"},
        SCISSORS: {"c"}
    }

    hand_scores = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3,
    }

    def __init__(self, hand: Union[str, int]):
        if isinstance(hand, int):
            self.hand = hand
        else:
            self.hand = next(
                rpc
                for rpc, vals in self.hands.items()
                if hand.lower() in vals
            )
        self.score = self.hand_scores[self.hand]


def pick_our_hand(opponent_hand: Hand, action: Action) -> Hand:
    if action.action == Action.WIN:
        if opponent_hand.hand == Hand.ROCK:
            return Hand(Hand.PAPER)
        if opponent_hand.hand == Hand.PAPER:
            return Hand(Hand.SCISSORS)
        if opponent_hand.hand == Hand.SCISSORS:
            return Hand(Hand.ROCK)

    if action.action == Action.DRAW:
        return opponent_hand

    if action.action == Action.LOSE:
        if opponent_hand.hand == Hand.ROCK:
            return Hand(Hand.SCISSORS)
        if opponent_hand.hand == Hand.PAPER:
            return Hand(Hand.ROCK)
        if opponent_hand.hand == Hand.SCISSORS:
            return Hand(Hand.PAPER)


def play_round(opponent_hand: Hand, action: Action) -> int:
    global WIN_BONUS, DRAW_BONUS

    our_hand = pick_our_hand(opponent_hand, action)

    if opponent_hand.hand == our_hand.hand:
        return DRAW_BONUS + our_hand.score

    if our_hand.hand == Hand.ROCK and opponent_hand.hand == Hand.SCISSORS:
        return WIN_BONUS + our_hand.score
    
    if our_hand.hand == Hand.SCISSORS and opponent_hand.hand == Hand.PAPER:
        return WIN_BONUS + our_hand.score

    if our_hand.hand == Hand.PAPER and opponent_hand.hand == Hand.ROCK:
        return WIN_BONUS + our_hand.score

    return our_hand.score


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    rounds = data.splitlines()

    score = sum(
        play_round(Hand(r.split()[0]), Action(r.split()[1]))
        for r in rounds
    )
    print(score)

