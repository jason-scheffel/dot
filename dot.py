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

import argparse
import os
import shutil
import subprocess
import time


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
    if args.add:
        pass
    elif args.remove:
        pass
    elif args.ignore:
        pass
    elif args.install:
        pass
    elif args.sync:
        pass
    elif args.init:
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

Note, this does not mean that this program can not be used without such
software; for instance, this program may include a Makefile to install itself,
but you need not be forced to use it.

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
        "type",
        choices=["file", "folder"],
        help="The type of file to add.",
    )

    sub_parser_add.add_argument(
        "file_or_folder",
        type=str,
        help="The file or folder to add to the dotfiles repo.",
    )

    sub_parser_add.add_argument(
        "dotfiles_repo",
        type=str,
        help="The path to the dotfiles repo.",
    )

    sub_parser_add.add_argument(
        "--no-git",
        action="store_true",
        help="Do not run git commands.",
        default=False,
    )

    # 'remove' subcommand
    sub_parser_remove = subparsers.add_parser(
        "remove",
        description="Remove a file or folder from the dotfiles repo.",
        help="Remove a file or folder from the dotfiles repo.",
        formatter_class=CustomFormatter,
    )

    sub_parser_remove.add_argument(
        "type",
        choices=["file", "folder"],
        help="The type of file to add.",
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
    sub_parser_remove.add_argument(
        "--no-git",
        action="store_true",
        help="Do not run git commands.",
        default=False,
    )

    # 'ignore' subcommand
    sub_parser_ignore = subparsers.add_parser(
        "ignore",
        description="Add a file or folder to the ignore list.",
        help="Add a file or folder to the ignore list.",
        formatter_class=CustomFormatter,
    )

    sub_parser_ignore.add_argument(
        "action",
        choices=["add", "remove"],
        help="The action to perform.",
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

    sub_parser_ignore.add_argument(
        "--no-git",
        action="store_true",
        help="Do not run git commands.",
        default=False,
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
        "--no-progress",
        action="store_true",
        help="Show progress bar.",
        default=False,
    )

    sub_parser_install.add_argument(
        "--quiet",
        action="store_true",
        help="Show no verbose output.",
        default=False,
    )

    # 'sync' subcommand
    sub_parser_sync = subparsers.add_parser(
        "sync",
        description="Sync the dotfiles repo.",
        help="Sync the dotfiles repo.",
        formatter_class=CustomFormatter,
    )

    sub_parser_sync.add_argument(
        "dotfiles_repo",
        type=str,
        help="The path to the dotfiles repo.",
    )

    sub_parser_sync.add_argument(
        "--no-progress",
        action="store_true",
        help="Show progress bar.",
        default=False,
    )

    sub_parser_sync.add_argument(
        "--quiet",
        action="store_true",
        help="Show no verbose output.",
        default=False,
    )

    sub_parser_sync.add_argument(
        "--no-git",
        action="store_true",
        default=False,
        help="Do not run git commands.",
    )

    # 'init' subcommand
    sub_parser_init = subparsers.add_parser(
        "init",
        description="Initialize the dotfiles repo.",
        help="Initialize the dotfiles repo.",
        formatter_class=CustomFormatter,
    )

    sub_parser_init.add_argument(
        "dotfiles_repo",
        type=str,
        help="The path to the dotfiles repo.",
        default=".",
    )

    sub_parser_init.add_argument(
        "--no-git-init",
        action="store_true",
        default=False,
        help="Do not initialize a git repo.",
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

dot.py ignore add file /nvim/plugin/packer_compiled.lua /foo/bar/dotfiles
- This will, in the dotfiles repo, ignore the above file.

dot.py ignore add folder ~/.config/idk/download/images /foo/bar/dotfiles
- This will, in the dotfiles repo, ignore the above folder.

dot.py ignore remove file /nvim/plugin/packer_compiled.lua /foo/bar/dotfiles
- This will, in the dotfiles repo, stop ignoring the above file.

{'*'*79}
* END EXAMPLES                                                                *
{'*'*79}"""
        print(examples_text)
        exit(0)

    return arguments


def check_arguments(args: argparse.Namespace) -> None:
    # check 'add'
    if args.sub_command == "add":
        if not os.path.exists(args.file_or_folder):
            print(f"File or folder does not exist: {args.file_or_folder}")
            exit(1)

        if not os.path.exists(args.dotfiles_repo):
            print(f"Dotfiles repo does not exist: {args.dotfiles_repo}")
            exit(1)

    # check 'remove'
    if args.sub_command == "remove":
        file_path_in_dotfiles_repo = os.path.join(
            args.dotfiles_repo, args.file_or_folder
        )
        if not os.path.exists(file_path_in_dotfiles_repo):
            print(
                f"File or folder does not exist in dotfiles repo: {file_path_in_dotfiles_repo}"  # noqa: E501
            )
            exit(1)

        if not os.path.exists(args.dotfiles_repo):
            print(f"Dotfiles repo does not exist: {args.dotfiles_repo}")
            exit(1)


if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)

#
