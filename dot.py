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

import argparse


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


def main(args: argparse.Namespace) -> None:
    pass


def assert_dependencies(args: argparse.Namespace) -> None:
    if args.no_dependencies_check:
        return


class CustomFormatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    """
    This formatter does the following:
        - Uses the default help formatter
        - Uses the raw description formatter
        - Sets the width to 79
    """

    def __init__(self, prog):
        super().__init__(prog, width=79)


def parse_args() -> argparse.Namespace:
    epilog = """
-------------------------------------------------------------------------------
This program requires, or optionally 'requires' other software.

Such software is listed in the README.md file that accompanies this program;
additionally, a copy of the said file can be found at:
<https://git.sr.ht/~jason-scheffel/dot>.

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
    parser = argparse.ArgumentParser(
        description="A tool for managing dotfiles.",
        epilog=epilog,
        formatter_class=CustomFormatter,
    )

    # show examples
    parser.add_argument(
        "-e",
        "--examples",
        action="store_true",
        help="show examples of how to use this program and exit",
        default=False,
    )

    subparsers = parser.add_subparsers(
        title="subcommands",
        description="valid subcommands",
        help="Do 'dot.py <subcommand> -h' for help on a subcommand.",
        dest="subcommand",
        required=True,
    )

    # 'add' subcommand
    sub_parser_add = subparsers.add_parser(
        "add",
        description="Add a file or folder to the dotfiles repo.",
        help="Add a file or folder to the dotfiles repo.",
        formatter_class=CustomFormatter,
    )

    sub_parser_add.add_argument(
        "file_or_folder",
        type=str,
        help="The file or folder to add to the dotfiles repo.",
    )

    # 'remove' subcommand
    sub_parser_remove = subparsers.add_parser(
        "remove",
        description="Remove a file or folder from the dotfiles repo.",
        help="Remove a file or folder from the dotfiles repo.",
        formatter_class=CustomFormatter,
    )

    sub_parser_remove.add_argument(
        "file_or_folder",
        type=str,
        help="The file or folder to remove from the dotfiles repo.",
    )

    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)

#
