#!/usr/bin/env python3
# filling_in_the_gaps.py — An exercise in organizing files.
# For more information, see README.md

from pathlib import Path
from dataclasses import dataclass
import logging
import os
import re
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


@dataclass
class SearchObject:
    directory: str
    prefix: str
    extension: str


def match_files(details: SearchObject) -> list[Path]:
    """Search directory for matching filenames and extensions, then return sorted list."""

    dir_path = Path.cwd() / details.directory
    file_list = list(dir_path.glob(f"{details.prefix}*.{details.extension}"))
    return sorted(file_list)

    # for index, match in enumerate(match_object):
    #     joined_file = "".join(match)
    #     old_path = f"{os.path.join(dir_path, joined_file)}"
    #     renamed_file = f"{match[0]}{(index + 1):03}{match[2]}"
    #     new_path = f"{os.path.join(dir_path, renamed_file)}"
    #     shutil.move(old_path, new_path)


def main():
    details = SearchObject(directory="spam", prefix="spam", extension="txt")
    matches = match_files(details)
    print(matches)


if __name__ == "__main__":
    main()
