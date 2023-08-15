#!/usr/bin/env python3
# filling_in_the_gaps.py — An exercise in organizing files.
# For more information, see README.md

import logging
from pathlib import Path
import os
import re
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def match_files(directory: str, prefix: str, extension: str) -> list[str]:
    """Search through filenames in specific folder and remove numeric gaps."""

    dir_path = Path.cwd() / directory
    file_list = list(dir_path.glob(f"{prefix}*.{extension}"))
    return sorted(file_list)

    # for index, match in enumerate(match_object):
    #     joined_file = "".join(match)
    #     old_path = f"{os.path.join(dir_path, joined_file)}"
    #     renamed_file = f"{match[0]}{(index + 1):03}{match[2]}"
    #     new_path = f"{os.path.join(dir_path, renamed_file)}"
    #     shutil.move(old_path, new_path)


def main():
    directory = input("Type name of directory: ")
    prefix = input("Please type prefix to match: ")
    extension = input("Please type extension to match: ")
    matches = match_files(directory, prefix, extension)
    for match in matches:
        print(match)


if __name__ == "__main__":
    main()
