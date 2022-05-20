import typing

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

    def get(self, key: int) -> T:
        """Get an object from the table"""
        return self.__content[key]

    def get_func(
        self, func: typing.Callable[[T], bool], limit: int = -1
    ) -> typing.Iterable[T]:
        """Get all objects from the table that match a condition"""

        yielded = 0

        for value in self.content.values():

            if not func(value):
                continue

            yield value

            yielded += 1

            if limit > 0 and yielded >= limit:
                break

    def get_many(self, keys: typing.Iterable[int]) -> typing.Iterable[T]:
        """Get multiple objects from the table"""
        return (self.__content[key] for key in keys)

    def insert(self, value: T) -> int:
        """Insert a new object into the table"""
        self.__content[
            i := (max(self.content.keys()) if len(self.content) > 0 else 0) + 1
        ] = value

        return i

    def delete(self, key: int) -> T:
        """Delete an object from the table"""
        return self.__content.pop(key)

    def update(self, key: int, value: T) -> None:
        """Update an object in the table"""
        self.__content[key] = value
