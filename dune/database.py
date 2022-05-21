import pickle
import zlib
import abc

from typing import TypeVar, Any, Dict

from .table import Table


__all__ = ["Database"]

T = TypeVar("T")


class Database(metaclass=abc.ABCMeta):
    """Manage all the tables"""

    def __init__(self) -> None:
        self.tables: Dict[str, Table] = {}

        for table in self.__annotations__:
            attr = getattr(self, table)

            if not isinstance(attr, Table):
                raise TypeError(f"{table} is not a Table")

            self.add_table(attr)

        if not len(self.tables):
            raise ValueError("No tables defined")

    def add_table(self, table: Table) -> None:
        """Add a table to the database"""
        self.tables[table.name] = table

    def get_table(self, name: str) -> Table:
        """Get table by name"""
        return self.tables[name]

    def export(self) -> Dict[str, Dict[int, Any]]:
        """Export the DB as a JSON"""
        return {name: table.content for name, table in self.tables.items()}

    def to_bin(self) -> bytes:
        """Serialize the DB as a zlib(pickle(dict))"""
        return zlib.compress(pickle.dumps(self.export()), level=9)

    @classmethod
    def from_bin(cls, data: bytes) -> 'Database':
        """Deserialize the DB from a zlib(pickle(dict))"""
        return pickle.loads(zlib.decompress(data))
