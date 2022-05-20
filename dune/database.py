import typing
import pickle
import zlib

from .table import Table


T = typing.TypeVar("T")


class Database(dict[str, Table]):
    """Manage all the tables"""

    def add_table(self, table: Table) -> None:
        """Add a table to the database"""
        self[table.name] = table

    def get_table(self, name: str) -> Table:
        return self[name]

    def export(self) -> dict[str, dict[int, typing.Any]]:
        """Export the DB as a JSON"""
        return {name: table.content for name, table in self.items()}

    def to_bin(self) -> bytes:
        """Serialize the DB as a zlib(pickle(dict))"""
        return zlib.compress(pickle.dumps(self.export()), level=9)

    @classmethod
    def from_bin(cls, data: bytes) -> "Database":
        """Deserialize the DB from a zlib(pickle(dict))"""
        return cls(pickle.loads(zlib.decompress(data)))