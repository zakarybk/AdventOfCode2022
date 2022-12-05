from pathlib import Path
from enum import IntEnum
from typing import List, Union


class RPC:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Score(tuple):
    pass


class PlayHand:

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

    win_bonus = 6

    def __init__(self, hand: str):
        self.hand = next(
            rpc
            for rpc, vals in self.hands.items()
            if hand.lower() in vals
        )


    def __eq__(self, other_hand: Union[RPC, 'PlayHand']) -> bool:
        if isinstance(other_hand, PlayHand): return self.hand == other_hand.hand
        return self.hand == other_hand

    
    def __gt__(self, other_hand: Union[RPC, 'PlayHand']) -> bool:
        if isinstance(other_hand, PlayHand): other_hand = other_hand.hand
        
        if self.hand == other_hand: return False
        if self.hand == RPC.ROCK and other_hand.RPC == RPC.SCISSORS: return True
        if self.hand == RPC.SCISSORS and other_hand.RPC == RPC.PAPER: return True
        if self.hand == RPC.PAPER and other_hand.RPC == RPC.ROCK: return True

        return False


    def against(self, other_hand: Union[RPC, 'PlayHand']) -> Score:
        if isinstance(other_hand, PlayHand): other_hand = other_hand.hand

        self_score = self.hand_scores[self.hand]
        other_score = self.hand_scores[other_hand]

        if self.hand == other_hand:
            hand_score = self_score
            self_score += hand_score
            other_score += hand_score
        else:
            if self.hand > other_hand:
                self_score += self.win_bonus
            else:
                other_score += self.win_bonus

        return Score((self_score,other_score))


data = Path("i.txt").read_text()


def play_round(ply1: str, ply2: str) -> Score:
    return PlayHand(ply1).against(PlayHand(ply2))


def play_game(game: str) -> Score:
    return map(
        lambda play: play_round(*play.split()),
        game.splitlines()
    )


print(sum(
    map(
        lambda player_scores: player_scores[1],
        play_game(data)
    )
))





