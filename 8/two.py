import numpy as np
from typing import List
from pathlib import Path
from functools import reduce

X = 1
Y = 0

max_or_0 = lambda vals: max(vals) if len(vals) else 0


# def is_visisble_from_top(x: int, y: int, forest: np.array) -> bool:
#     return bool(max_or_0(forest[:y,x]) < forest[y,x]) or y == 0


# def is_visisble_from_bottom(x: int, y: int, forest: np.array) -> bool:
#     return bool(max_or_0(forest[y+1:,x][::-1]) < forest[y,x]) or y == forest.shape[Y]-1


# def is_visisble_from_left(x: int, y: int, forest: np.array) -> bool:
#     return bool(max_or_0(forest[y,:x]) < forest[y,x]) or x == 0


# def is_visisble_from_right(x: int, y: int, forest: np.array) -> bool:
#     return bool(max_or_0(forest[y,x+1:][::-1]) < forest[y,x]) or x == forest.shape[X]-1

mul = lambda a,b: a*b


def viewing_distance(og_tree: int, trees: np.array) -> int:
    if not len(trees): return trees
    distance = 0
    ts = []

    for tree in trees:
        # print(trees)
        if tree < og_tree:
            distance += 1
            ts.append(tree)
        else:
            break
        # elif tree >= og_tree:
        #     distance += 1
        #     ts.append(tree)
        #     break

    return len(set(ts))


def viewing_trees(og_tree: int, trees: np.array) -> int:
    if not len(trees): return trees
    distance = 0
    ts = []

    for tree in trees:
        # print(trees)
        if tree < og_tree:
            distance += 1
            ts.append(tree)
        elif tree >= og_tree:
            distance += 1
            ts.append(tree)
            break

    return ts


def trees_blocking_top(x: int, y: int, forest: np.array, fn=viewing_distance) -> int:
    return fn(forest[y,x], forest[:y,x][::-1])


def trees_blocking_bottom(x: int, y: int, forest: np.array, fn=viewing_distance) -> int:
    return fn(forest[y,x], forest[y+1:,x])


def trees_blocking_left(x: int, y: int, forest: np.array, fn=viewing_distance) -> int:
    return fn(forest[y,x], forest[y,:x][::-1])


def trees_blocking_right(x: int, y: int, forest: np.array, fn=viewing_distance) -> int:
    return fn(forest[y,x], forest[y,x+1:])


def count_visible_in_forest(forest: np.array) -> int:
    calc_blocking = [
        trees_blocking_top,
        trees_blocking_bottom,
        trees_blocking_left,
        trees_blocking_right
    ]
    # print(list(map(lambda calc: calc(15,5,forest), calc_blocking)))


    def scenic_score(vals):
        return reduce(mul, vals) if len(vals) else 0

    max_vals = [[],[],[]]
    pos = ()
    best_trees = {}

    for y in range(forest.shape[Y]):
        for x in range(forest.shape[X]):
            distances = []
            trees = []
            for block in calc_blocking:
                d = block(x,y, forest)
                if d:
                    distances.append(d)
                    # trees.append(d[1])
            
            # distance, vals = list(map(lambda calc: calc(x,y, forest), calc_blocking))
            if scenic_score(distances) > scenic_score(max_vals[0]):
                max_vals = [distances]
                pos = (x,y)

                for block in calc_blocking:
                    best_trees[block.__name__] = block(x,y,forest,fn=viewing_trees)

    print(pos)
    print(best_trees)
    print(f"scores: {max_vals[0]}")
    np.set_printoptions(threshold=np.inf)
    # print(f"pos: {x},{y}")
    # for i, thing in enumerate(max_vals[1]):
    #     print(max_vals[0][i], thing)

    # print(list(map(lambda x: len(x), max_vals[1])))
    # together = reduce(mul, list(map(lambda x: max_vals[1])))
    # print(together)

    together = scenic_score(max_vals[0])

    return together
            # print(max(val))
    # print(max_vals[0])

    # vals = sorted(list(
    #     map(
    #         lambda xy : list(map(lambda calc: calc(xy[0], xy[0], forest), calc_blocking)),
    #         list((x,y) for y in range(forest.shape[Y]) for x in range(forest.shape[X]))
    #     )
    # ), key=sum)
    # print(vals[0])

    # print(max(
    #     reduce(mul, list(map(lambda calc: calc(x,y,forest), calc_blocking)))
    #     for y in range(forest.shape[Y]) for x in range(forest.shape[X])
    # ))


def txt_to_forest(data: str) -> np.array:
    return np.array([[int(tree) for tree in line] for line in data.splitlines()])


if __name__ == '__main__':
    data = Path("i.txt").read_text()

    arr = txt_to_forest(data)
    visible = count_visible_in_forest(arr)
    print(visible)