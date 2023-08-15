#!/usr/bin/env python3
# filling_in_the_gaps.py — An exercise in organizing files.
# For more information, see README.md

from pathlib import Path
from dataclasses import dataclass
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


@dataclass
class FileInfo:
    directory: str
    prefix: str
    extension: str


def find_matches(info: FileInfo) -> list[Path]:
    """Search subdirectory in cwd for matching filenames and extensions, and return sorted list."""
    path = Path.cwd() / info.directory
    matches = list(path.glob(f"{info.prefix}*.{info.extension}"))
    return sorted(matches)


def reorder_sequence(matches: list[Path]) -> list[str]:
    """Slice number info from first item in matches and create list of sequential values."""
    first_item = str(matches[0])[-7:-4]
    new_sequence = [
        f"{(int(first_item) + index):03}" for index, _ in enumerate(matches)
    ]
    return new_sequence


def fill_gaps(info: FileInfo, matches: list[Path], sequence: list[str]) -> None:
    """Iterate over matches list items and rename files sequentially."""
    for index, match in enumerate(matches):
        match.rename(
            f"{info.directory}/{info.prefix}{sequence[index]}.{info.extension}"
        )


def main() -> None:
    """Main sequence."""
    info_1: FileInfo = FileInfo(directory="spam", prefix="spam", extension="txt")
    matches: list[Path] = find_matches(info_1)
    sequence: list[str] = reorder_sequence(matches)
    fill_gaps(info_1, matches, sequence)


if __name__ == "__main__":
    main()
