#!/usr/bin/env python3
# filling_in_the_gaps.py — An exercise in organizing files.
# For more information, see README.md

from pathlib import Path
from dataclasses import dataclass
import logging
import os
import shutil

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
    """Search directory for matching filenames and extensions, then return sorted list."""

    path = Path.cwd() / details.directory
    matches = list(path.glob(f"{details.prefix}*.{details.extension}"))
    return sorted(matches)


def fill_gaps(matches):
    print(matches[0].name)
    # for index, match in enumerate(match_object):
    #     joined_file = "".join(match)
    #     old_path = f"{os.path.join(dir_path, joined_file)}"
    #     renamed_file = f"{match[0]}{(index + 1):03}{match[2]}"
    #     new_path = f"{os.path.join(dir_path, renamed_file)}"
    #     shutil.move(old_path, new_path)


def main():
    m1 = Match(directory="spam", prefix="spam", extension="txt")
    matches = find_matches(m1)
    fill_gaps(matches)


if __name__ == "__main__":
    main()
