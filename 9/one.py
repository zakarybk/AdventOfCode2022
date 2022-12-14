import math
from enum import Enum
from typing import Union, Tuple, List
from pathlib import Path
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Vec2:
    x: int
    y: int


    def distance(self, other: 'Vec2') -> int:
        return math.ceil(math.dist(self, other))


    def direction(self, other: 'Vec2') -> 'Vec2':
        return (other-self).normalise()

    
    def normalise(self) -> 'Vec2':
        longest = max(map(abs, self))
        if not longest: return Vec2(0,0)
        return Vec2(
            x=math.ceil(self.x/longest),
            y=math.ceil(self.y/longest)
        )


    def __iter__(self):
        for field in ('x','y'):
            yield getattr(self, field)


    def __add__(self, other: 'Vec2'):
        return Vec2(
            x=self.x+other.x,
            y=self.y+other.y
        )

    
    def __sub__(self, other: 'Vec2'):
        return Vec2(
            x=self.x-other.x,
            y=self.y-other.y
        )


    def __mul__(self, mul: int):
        return Vec2(
            x=self.x*mul,
            y=self.y*mul
        )

    
    def __hash__(self):
        return hash((self.x, self.y))
        


@dataclass
class Direction:
    UP = Vec2(0,1)
    DOWN = Vec2(0,-1)
    LEFT = Vec2(-1,0)
    RIGHT = Vec2(1,0)


def command_to_direction(command: str) -> Direction:
    mapping = {
        'r': Direction.RIGHT,
        'u': Direction.UP,
        'l': Direction.LEFT,
        'd': Direction.DOWN
    }
    return mapping.get(command.lower(), Vec2(0,0))


def step(head: Vec2, tail: Vec2, direction: Vec2) -> Tuple[Vec2, Vec2]:
    old_head = head
    head += direction

    if tail.distance(head) >= 2:
        if tail.direction(head) in {Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT}:
            tail = old_head
        elif tail.distance(head) == 3:
            tail = old_head

    return head, tail


def run(commands: List[str]) -> int:
    head = Vec2(0,0)
    tail = Vec2(0,0)
    tail_visits = set()
    history = [[head],[None]]

    for command in commands:
        direction = command_to_direction(command.split()[0])
        distance = int(command.split()[1])

        for _ in range(distance):
            head, tail = step(head, tail, direction)
            if tail not in tail_visits:
                tail_visits.add(tail)

            history[0].append(head)
            history[1].append(tail)

    return len(tail_visits), history


def draw_board(head: Vec2, tail: Vec2, size: Vec2):
    board = ""
    start = Vec2(0,0)

    for row in range(size.y):
        board_row = ""
        for col in range(size.x):
            pos = Vec2(col, row)
            if pos == head:
                board_row += 'H'
            elif pos == tail:
                board_row += 'T'
            elif pos == start:
                board_row += 'S'
            else:
                board_row += '.'
        board = board_row + '\n' + board

    return board


def generate_board(history: List) -> str:
    plays = []
    board_size = Vec2(6,5)

    for head, tail in zip(history[0], history[1]):
        plays.append(draw_board(head, tail, board_size))

    return '\n\n'.join(plays)


if __name__ == '__main__':
    data = Path("i.txt").read_text()

    visits, _ = run(data.splitlines())
    print(visits)