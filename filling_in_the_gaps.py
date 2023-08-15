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
logging.disable(logging.CRITICAL)  # Note out to enable logging.


@dataclass
class Match:
    directory: str
    prefix: str
    extension: str


def find_matches(details: Match) -> list[Path]:
    """Search subdirectory in cwd for matching filenames and extensions, then return sorted list."""
    path = Path.cwd() / details.directory
    matches = list(path.glob(f"{details.prefix}*.{details.extension}"))
    return sorted(matches)


def fill_gaps(details: Match, matches: list[Path]) -> None:
    """Rename files beginning at index of 1."""
    for index, match in enumerate(matches):
        match.rename(
            f"{details.directory}/{details.prefix}{(index + 1):03}.{details.extension}"
        )


def main() -> None:
    """Main sequence."""
    details_1 = Match(directory="spam", prefix="spam", extension="txt")
    matches = find_matches(details_1)
    fill_gaps(details_1, matches)


if __name__ == "__main__":
    main()
