from operator import mul
from typing import Callable, List, Tuple
from pathlib import Path
from functools import reduce


mul_reduce: Callable[[Tuple[int, int]], Callable[[Tuple[int, int]], int]] = \
    lambda vals: reduce(mul, vals)


def run(commands: List[str], check: Callable[[int], bool]) -> List[Tuple[int, int]]:
    """ [(x, cycle), ...] """
    cycle: int = 1
    x: int = 1
    signal_strengths: List[Tuple[int, int]] = []

    for cmd in commands:
        if cmd == 'noop':
            if check(cycle):
                signal_strengths.append((x, cycle))
            cycle += 1
        else:
            for _ in range(2):
                if check(cycle):
                    signal_strengths.append((x, cycle))
                cycle += 1

            signal: str = cmd.split()[1]
            x += int(signal)

    return signal_strengths


def sum_signals(signals: List[Tuple[int, int]]) -> int:
    return sum(map(mul_reduce, signals))


if __name__ == '__main__':
    data = Path("i.txt").read_text()

    signals = run(data.splitlines(), check=lambda i: i in [20, 60, 100, 140, 180, 220])
    print(signals)
    print(sum_signals(signals))
