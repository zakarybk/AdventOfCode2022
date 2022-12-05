from typing import Tuple, List
from pathlib import Path


LOWER_CASE_OFFSET = 1
UPPER_CASE_OFFSET = 27


def item_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord('A') + UPPER_CASE_OFFSET
    return ord(item) - ord('a') + LOWER_CASE_OFFSET


def common_items(*item_sets: List[set]) -> str:
    return ''.join(set.intersection(*item_sets))


def total_priorities(backpacks: List[str]):
    return sum(
        sum(map(item_priority, common_items(*map(set, backpacks[i:i+3]))))
        for i in range(0, len(backpacks), 3)
    )


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    backpacks = data.splitlines()

    total_priority = total_priorities(backpacks)

    print(total_priority)