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
class Match:
    directory: str
    prefix: str
    extension: str


def find_matches(details: Match) -> list[Path]:
    """Search subdirectory in cwd for matching filenames and extensions, and return sorted list."""
    path = Path.cwd() / details.directory
    matches = list(path.glob(f"{details.prefix}*.{details.extension}"))
    return sorted(matches)


def reorder_sequence(matches):
    """Slice number info from first item in matches and create list of sequential values."""
    first_item = str(matches[0])[-7:-4]
    new_sequence = [
        f"{(int(first_item) + index):03}" for index, _ in enumerate(matches)
    ]
    return new_sequence


def fill_gaps(details: Match, matches: list[Path], sequence: list[str]) -> None:
    """Iterate over matches list items and rename files sequentailly."""
    for index, match in enumerate(matches):
        match.rename(
            f"{details.directory}/{details.prefix}{sequence[index]}.{details.extension}"
        )


def main() -> None:
    """Main sequence."""
    details_1 = Match(directory="spam", prefix="spam", extension="txt")
    matches = find_matches(details_1)
    sequence = reorder_sequence(matches)
    fill_gaps(details_1, matches, sequence)


if __name__ == "__main__":
    main()
