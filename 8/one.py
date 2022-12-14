import numpy as np
from typing import List
from pathlib import Path

X = 1
Y = 0

max_or_0 = lambda vals: max(vals) if len(vals) else 0


def is_visisble_from_top(x: int, y: int, forest: np.array) -> bool:
    return bool(max_or_0(forest[:y,x]) < forest[y,x]) or y == 0


def is_visisble_from_bottom(x: int, y: int, forest: np.array) -> bool:
    return bool(max_or_0(forest[y+1:,x][::-1]) < forest[y,x]) or y == forest.shape[Y]-1


def is_visisble_from_left(x: int, y: int, forest: np.array) -> bool:
    return bool(max_or_0(forest[y,:x]) < forest[y,x]) or x == 0


def is_visisble_from_right(x: int, y: int, forest: np.array) -> bool:
    return bool(max_or_0(forest[y,x+1:][::-1]) < forest[y,x]) or x == forest.shape[X]-1


def count_visible_in_forest(forest: np.array) -> int:
    checks = [
        is_visisble_from_top,
        is_visisble_from_bottom,
        is_visisble_from_left,
        is_visisble_from_right
    ]
    return sum(
        any(map(lambda check: check(x,y,forest), checks))
        for y in range(forest.shape[Y]) for x in range(forest.shape[X])
    )


def txt_to_forest(data: str) -> np.array:
    return np.array([[int(tree) for tree in line] for line in data.splitlines()])


if __name__ == '__main__':
    data = Path("i.txt").read_text()

    arr = txt_to_forest(data)
    visible = count_visible_in_forest(arr)
    print(visible)