import typing
import re

__alL__ = ["Table", "TableStr"]

T = typing.TypeVar("T")


class Table(typing.Generic[T]):
    """Database table object"""

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__content: dict[int, T] = {}

    @property
    def name(self) -> str:
        """Get the name of the table"""
        return self.__name

    @property
    def content(self) -> dict[int, T]:
        """Get the full content of the table"""
        return self.__content

    def get(self, key: int) -> T | int:
        """Get an object from the table"""
        return self.__content.get(key, -1)

    def get_key_from_value(self, value: T) -> int:
        """Get the key of an object in the table"""
        return next(
            (key for key, val in self.__content.items() if val == value), -1
        )

    def get_func(
        self, func: typing.Callable[[T], bool], limit: int = -1
    ) -> typing.Iterable[tuple[int, T]]:
        """Get all objects from the table that match a condition"""
        yielded = 0

        for key, value in self.content.items():

            if not func(value):
                continue

            yield key, value

            yielded += 1

            if limit > 0 and yielded >= limit:
                break

    def get_many(self, keys: typing.Iterable[int]) -> typing.Iterable[T]:
        """Get multiple objects from the table"""
        return (self.__content[key] for key in keys)

    def insert(self, value: T) -> int:
        """Insert a new object into the table"""
        key = max(self.content.keys()) + 1 if len(self.content) > 0 else 0
        self.__content[key] = value
        return key

    def delete(self, key: int) -> T:
        """Delete an object from the table"""
        return self.__content.pop(key)

    def update(self, key: int, value: T) -> None:
        """Update an object in the table"""
        self.__content[key] = value


class TableStr(typing.Generic[T], Table[str]):
    """Table of strings"""

    def search(self, value: str) -> typing.Iterable[tuple[int, str]]:
        """Search for a string in the table"""
        return self.get_func(lambda val: value in val)

    def search_regex(self, regex: str) -> typing.Iterable[tuple[int, str]]:
        """Search for a regex in the table"""
        return self.get_func(lambda val: re.match(regex, val) is not None)
