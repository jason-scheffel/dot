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
Please the following messgae. I understand, however, that you may not wish to
keep seeing the message. If that is the case, you may run this program with the
'-H' flag to hide the message. '-H' is the same as '-h' except that it hides
the message.

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

    # show help without epilog
    parser.add_argument(
        "-H",
        "--no-epilog",
        action="store_true",
        help="show help without epilog",
        default=False,
    )

    subparsers = parser.add_subparsers(
        title="subcommands",
        description="valid subcommands",
        help="Do 'dot.py <subcommand> -h' for help on a subcommand.",
        dest="subcommand",
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

    # 'ignore' subcommand
    sub_parser_ignore = subparsers.add_parser(
        "ignore",
        description="Add a file or folder to the ignore list.",
        help="Add a file or folder to the ignore list.",
        formatter_class=CustomFormatter,
    )

    sub_parser_ignore.add_argument(
        "type",
        choices=["file", "folder"],
        help="The type of file to ignore.",
    )

    sub_parser_ignore.add_argument(
        "file_or_folder",
        type=str,
        help="The file or folder to ignore.",
    )

    sub_parser_ignore.add_argument(
        "dotfiles_repo",
        type=str,
        help="The path to the dotfiles repo.",
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

    sub_parser_remove.add_argument(
        "dotfiles_repo",
        type=str,
        help="The path to the dotfiles repo.",
    )

    # 'install' subcommand
    sub_parser_install = subparsers.add_parser(
        "install",
        description="Install the dotfiles repo.",
        help="Install the dotfiles repo.",
        formatter_class=CustomFormatter,
    )

    sub_parser_install.add_argument(
        "dotfiles_repo",
        type=str,
        help="The path to the dotfiles repo.",
    )

    sub_parser_install.add_argument(
        "-p",
        "--progress",
        action="store_true",
        help="Show progress bar.",
        default=True,
    )

    sub_parser_install.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show verbose output.",
        default=True,
    )

    arguments = parser.parse_args()

    if arguments.no_epilog:
        parser.epilog = None
        print(parser.format_help())

    if arguments.examples:
        examples_text = f"""{'*'*79}
* EXAMPLES                                                                    *
{'*'*79}

dot.py add ~/.xinitrc /foo/bar/dotfiles
- Adds the file, ~/.xinitrc, to the dotfiles repo.

dot.py remove ~/.xinitrc /foo/bar/dotfiles
- Removes the file, ~/.xinitrc, from the dotfiles repo.

dot.py install /foo/bar/dotfiles
- This will install the dotfiles in /foo/bar/dotfiles to the system.

{'*'*79}
* END EXAMPLES                                                                *
{'*'*79}"""
        print(examples_text)
        exit(0)

    return arguments


if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)

#
