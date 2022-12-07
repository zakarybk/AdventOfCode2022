from pathlib import Path


MARKER_LEN = 4


def all_different(chars: str) -> bool:
    return len(set(chars)) == len(chars)


def pos_of_marker(data: str) -> int:
    return next(
        pos+MARKER_LEN
        for pos in range(len(data)-MARKER_LEN)
        if all_different(data[pos:pos+MARKER_LEN])
    )


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    print(pos_of_marker(data))
