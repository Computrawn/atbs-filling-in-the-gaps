#! python3
"""filling_in_the_gaps — An exercise in organizing files.
For more information, see project_details.txt."""

from pathlib import Path
import os
import re
import shutil


def filling_in_the_gaps():
    """Search through filenames in specific folder and remove numeric gaps."""
    dir_path = Path(os.getcwd(), "spam")
    filename_regex = re.compile(r"(spam)(\d{3})(\.txt)")

    for f_name in os.listdir(dir_path):
        file_list.append(f_name)

    list.sort(file_list)
    file_str = ", ".join(file_list)
    match_object = filename_regex.findall(file_str)

    for idx, f_match in enumerate(match_object):
        joined_file = "".join(f_match)
        old_path = f"{os.path.join(dir_path, joined_file)}"
        renamed_file = f"{f_match[0]}00{idx + 1}{f_match[2]}"
        new_path = f"{os.path.join(dir_path, renamed_file)}"
        shutil.move(old_path, new_path)


file_list = []
filling_in_the_gaps()
