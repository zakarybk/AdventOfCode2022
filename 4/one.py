from pathlib import Path
from typing import Generator, Tuple


def section_split(section: str) -> Tuple[int, int]:
    start, sep, end = section.partition('-')
    return int(start), int(end)+1


def elf_split(section_pair: str) -> Tuple[str, str]:
    start, sep, end = section_pair.partition(',')
    return start, end


def sections_overlap(first_section: str, second_section: str) -> bool:
    first_start, first_end = section_split(first_section)
    second_start, second_end = section_split(second_section)

    if first_start <= second_start and first_end >= second_end:
        return True

    if second_start <= first_start and second_end >= first_end:
        return True

    return False


if __name__ == '__main__':
    data = Path("i.txt").read_text()
    elf_sections = data.splitlines()

    total = sum(
        sections_overlap(*elf_split(elf_pair))
        for elf_pair in elf_sections
    )

    print(total)