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


def filling_in_the_gaps():
    """Search through filenames in specific folder and remove numeric gaps."""
    dir_path = Path(os.getcwd(), "spam")
    filename_regex = re.compile(r"(spam)(\d{3})(\.txt)")

    file_list = [file_name for file_name in os.listdir(dir_path)]

    list.sort(file_list)
    file_str = ", ".join(file_list)
    match_object = filename_regex.findall(file_str)

    for index, match in enumerate(match_object):
        joined_file = "".join(match)
        old_path = f"{os.path.join(dir_path, joined_file)}"
        renamed_file = f"{match[0]}{(index + 1):03}{match[2]}"
        new_path = f"{os.path.join(dir_path, renamed_file)}"
        shutil.move(old_path, new_path)


def main():
    filling_in_the_gaps()


if __name__ == "__main__":
    main()
