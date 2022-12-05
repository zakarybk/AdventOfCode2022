from typing import Tuple, List
from pathlib import Path


LOWER_CASE_OFFSET = 1
UPPER_CASE_OFFSET = 27


def item_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord('A') + UPPER_CASE_OFFSET
    return ord(item) - ord('a') + LOWER_CASE_OFFSET


def common_items(first_compartment: str, second_compartment: str) -> str:
    return ''.join(set(first_compartment).intersection(set(second_compartment)))


def split_backpack(backpack: str) -> Tuple[str, str]:
    half = int(len(backpack) / 2)
    return backpack[:half], backpack[half:]


def total_priorities(backpacks: List[str]) -> int:
    return sum(
        sum(map(item_priority, common_items(*split_backpack(backpack))))
        for backpack in backpacks
    )


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    backpacks = data.splitlines()

    total_priority = total_priorities(backpacks)

    print(total_priority)