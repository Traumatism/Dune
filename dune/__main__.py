import argparse
import requests
import sys


from typing import Iterator, Type
from urllib3 import disable_warnings

from dune import console, version, author
from dune.common.base import DuneModule

from dune.modules.public_snippets import PublicSnippets
from dune.modules.user_enum import UserEnum

MODULES = {PublicSnippets, UserEnum}


def get_modules() -> Iterator[Type[DuneModule]]:
    """ Get modules """
    for module in MODULES:
        if issubclass(module, DuneModule):
            yield module


if __name__ == "__main__":
    disable_warnings()

    console.print(
        r"""[yellow]
[orange3]/\_/\ [/orange3] [bold]Dune v%(version)s[/bold]
[orange3]\, ,/[/orange3]  [dim]A Gitlab pwning tool[/dim]
[orange3] \_/ [/orange3]  [red]Author: %(author)s[/red]
[/yellow]
        """ % {"version": version, "author": author}
    )

    parser = argparse.ArgumentParser()

    target_specification = parser.add_argument_group(
        "TARGET SPECIFICATION", description="Define the target(s) to scan"
    )

    target_specification.add_argument(
        "-t", "--target",
        type=str,
        required=False,
        help="Target to scan",
        metavar="<url>",
        dest="target",
        default=""
    )

    target_specification.add_argument(
        "-l", "--list",
        type=str,
        required=False,
        help="Path to file with URLs",
        metavar="<path>",
        dest="path",
        default=""
    )

    arguments = parser.parse_args()

    if (
        tuple(map(bool, (arguments.target, arguments.path)))
        in ((True, True), (False, False))
    ):
        console.log(
            "You must specify a single target "
            "[underline]or[/underline] a file path."
        )

        sys.exit(0)

    if arguments.path:
        console.log("Not implemented yet.")
        sys.exit(0)

    console.log(f"Connecting to '{arguments.target}'")

    try:
        response = requests.get(arguments.target, verify=False)
    except requests.exceptions.RequestException:
        console.log("Can't connect to target.")
        sys.exit(0)

    console.log("Target is up and running.")

    for module in get_modules():
        console.log(f"Running module '{module.name}' {module.description}")
        module(arguments.target).run()

    console.log("Done!")
