import re
from pathlib import Path
from typing import List, Deque
from collections import deque
from dataclasses import dataclass


@dataclass
class Move:
    count: int
    source: int
    target: int


def parse_moves(data: str) -> str:
    lines = data.splitlines()
    moves_data = ""
    at_start = False
    for line in lines:
        if at_start: moves_data += line + '\n'
        if line == '': at_start = True
    return moves_data


def parse_stacks(data: str) -> str:
    lines = data.splitlines()
    stack_data = ""
    for line in lines:
        if line == '': break
        stack_data += line + '\n'
    return stack_data


def make_stacks(stack_data: str) -> List[Deque[str]]:
    lines = stack_data.splitlines()
    cols = int(len(lines[0]) / 4) + 1 # col width = 4
    stacks = list(map(lambda x: deque(), range(cols))) # [deque()]*5 created same obj :(

    for line in lines:
        for i, col_i in enumerate(range(1, len(lines[0]), 4)):
            col = line[col_i]
            if ord(col) in range(ord('A'), ord('Z')+1):
                stacks[i].appendleft(col)

    return stacks


move_regex = re.compile("move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)", re.IGNORECASE)
def parse_move(move: str) -> Move:
    m = move_regex.match(move)
    return Move(
        count=int(m.group(1)),
        source=int(m.group(2))-1,
        target=int(m.group(3))-1 # source counts from 1, stack 0
    )


def run(data: str) -> str:
    stacks = make_stacks(parse_stacks(data))
    moves = parse_moves(data).splitlines()

    for move in map(parse_move, moves):
        for count in range(move.count):
            item = stacks[move.source].pop()
            stacks[move.target].append(item)
            print(f"Moved {item} from {move.source} to {move.target}")

    
    tops = ''
    for stack in stacks:
        val = stack.pop()
        tops += val

    return tops

if __name__ == '__main__':
    data = Path("i.txt").read_text()

    tops = run(data)

    print(tops)


