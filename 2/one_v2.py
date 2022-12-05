from pathlib import Path
from enum import IntEnum
from typing import List, Union


WIN_BONUS = 6
DRAW_BONUS = 3


class RPC:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Hand:
    hands = {
        RPC.ROCK: {"a", "x"},
        RPC.PAPER: {"b", "y"},
        RPC.SCISSORS: {"c", "z"}
    }

    hand_scores = {
        RPC.ROCK: 1,
        RPC.PAPER: 2,
        RPC.SCISSORS: 3,
    }

    def __init__(self, hand: str):
        self.hand = next(
            rpc
            for rpc, vals in self.hands.items()
            if hand.lower() in vals
        )
        self.score = self.hand_scores[self.hand]



def play_round(opponent_hand: Hand, our_hand: Hand) -> int:
    global WIN_BONUS, DRAW_BONUS

    if opponent_hand.hand == our_hand.hand:
        return DRAW_BONUS + our_hand.score

    if our_hand.hand == RPC.ROCK and opponent_hand.hand == RPC.SCISSORS:
        return WIN_BONUS + our_hand.score
    
    if our_hand.hand == RPC.SCISSORS and opponent_hand.hand == RPC.PAPER:
        return WIN_BONUS + our_hand.score

    if our_hand.hand == RPC.PAPER and opponent_hand.hand == RPC.ROCK:
        return WIN_BONUS + our_hand.score

    return our_hand.score


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    rounds = data.splitlines()

    score = sum(
        play_round(*map(Hand, r.split()))
        for r in rounds
    )
    print(score)

