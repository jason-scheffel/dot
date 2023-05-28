"""
SPDX-FileCopyrightText: 2023 Jason Scheffel <contact@jasonscheffel.com>
SPDX-License-Identifier: AGPL-3.0-or-later

Copyright (C) 2023 Jason Scheffel

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import csv
import os
import shutil
import subprocess
import time

from argparse import Namespace


def run(cmd: str) -> dict[str, str | int]:
    cmd_out = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    return {
        "stdout": cmd_out.stdout,
        "stderr": cmd_out.stderr,
        "returncode": cmd_out.returncode,
    }


def yeet_metadata(file_path: str) -> None:
    """
    Given a file, remove all metadata from it.
    """
    pass


def get_stem(file_path: str) -> str:
    """
    Given a file or dir path, return the stem of the path.

    For example, /home/usr/file.txt would return /home/usr.
    """

    return os.path.dirname(file_path)


def add_file(file_path: str) -> None:
    pass


def remove_file(file_path: str) -> None:
    pass


def add_folder(folder_path: str) -> None:
    pass


def remove_folder(folder_path: str) -> None:
    pass


def main(args: Namespace) -> None:
    pass


def assert_dependencies(args: Namespace) -> None:
    if args.no_dependencies_check:
        return


if __name__ == "__main__":
    main(arguments)

#
