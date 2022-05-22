import re

from typing import (
    TypeVar,
    Generic,
    Callable,
    Iterable,
    Tuple,
    Union,
    Dict,
)


__all__ = ["Table", "TableStr"]

T = TypeVar("T")
Row = Tuple[int, T]


class Table(Generic[T]):
    """Database table object"""

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__content: Dict[int, T] = {}

    @property
    def content(self) -> Dict[int, T]:
        """Get the table content"""
        return self.__content

    @property
    def name(self) -> str:
        """Get the name of the table"""
        return self.__name

    def get(self, key: int) -> Union[T, int]:
        """Get an object from the table"""
        return self.content.get(key, -1)

    def get_key_from_value(self, value: T) -> int:
        """Get the key of an object in the table"""
        return next(
            (key for key, val in self.content.items() if val == value), -1
        )

    def get_func(
        self,
        func: Callable[[T], bool],
        limit: int = -1,
    ) -> Iterable[Row]:
        """Get all objects from the table that match a condition"""
        yielded = 0

        for key, value in self.content.items():

            if func(value) is False:
                continue

            yield key, value

            yielded += 1

            if limit > 0 and yielded >= limit:
                break

    def get_many(self, keys: Iterable[int]) -> Iterable[Row]:
        """Get multiple objects from the table"""
        yield from ((key, self.get(key)) for key in keys)

    def insert(self, value: T) -> int:
        """Insert a new object into the table"""
        key = max(self.content.keys()) + 1 if len(self.content) > 0 else 0

        self.__content[key] = value

        return key

    def insert_many(self, values: Iterable[T]) -> Iterable[int]:
        """Insert multiple objects into the table"""
        yield from map(self.insert, values)

    def delete(self, key: int) -> None:
        """Delete an object from the table"""
        del self.__content[key]

    def pop(self, key: int) -> T:
        """Pop an object from the table"""
        return self.__content.pop(key)

    def update(self, key: int, value: T) -> None:
        """Update an object in the table"""
        self.__content.update({key: value})


class TableStr(Table[str]):
    """Table of strings"""

    def search(self, value: str) -> Iterable[Tuple[int, str]]:
        """Search for a string in the table"""
        return self.get_func(lambda x: value in x)

    def search_regex(self, regex: str) -> Iterable[Tuple[int, str]]:
        """Search for a regex in the table"""
        return self.get_func(lambda x: re.match(regex, x) is not None)
