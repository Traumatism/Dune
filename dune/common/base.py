import re

from abc import ABC
from dataclasses import dataclass

from rich.console import RenderableType

from .. import console


@dataclass
class BaseType:

    def render(self) -> RenderableType | str:
        """ Render the object """
        return str(self)

    def __rich_console__(self, console, options):
        """ Render the object """
        return self.render()


class DuneModule(ABC):
    """ Base class for all modules """
    name: str
    description: str

    def __init__(self, target: str) -> None:
        """ Initialize the module """
        self.target = target
        self.console = console
        self.__headers = {}

    @property
    def headers(self) -> dict[str, str | int | dict]:
        """ Get headers """
        return self.__headers

    def add_headers(self, key: str, value: str | int | dict) -> None:
        """ Add a row to headers """
        self.__headers[key] = value

    @property
    def host(self) -> str:
        """ Return the hostname of the URL """
        match = re.search(r"^(?:https?:\/\/)?(?:[^@]+@)?([^:/]+)", self.target)
        return match.group(1) if match else "127.0.0.1"

    def run(self) -> None:
        """ Run the module """
        raise NotImplementedError("run() not implemented")
