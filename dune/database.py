import typing
import pickle
import zlib
import abc

from .table import Table


T = typing.TypeVar("T")


class Database(metaclass=abc.ABCMeta):
    """Manage all the tables"""

    def __init__(self) -> None:
        self.tables: dict[str, Table] = {}

        for annotation in self.__annotations__:

            obj: Table = self.__getattribute__(annotation)

            self.add_table(obj)

    @property
    def content(self) -> dict[str, dict[int, typing.Any]]:
        """Export the DB as a JSON"""
        return self.export()

    def add_table(self, table: Table) -> None:
        """Add a table to the database"""
        self.tables[table.name] = table

    def get_table(self, name: str) -> Table:
        return self.tables[name]

    def export(self) -> dict[str, dict[int, typing.Any]]:
        """Export the DB as a JSON"""
        return {name: table.content for name, table in self.tables.items()}

    def to_bin(self) -> bytes:
        """Serialize the DB as a zlib(pickle(dict))"""
        return zlib.compress(pickle.dumps(self.export()), level=9)

    # @classmethod
    # def from_bin(cls, data: bytes) -> "Database":
    #     """Deserialize the DB from a zlib(pickle(dict))"""
    #     return cls(pickle.loads(zlib.decompress(data)))
