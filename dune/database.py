import abc

from typing import TypeVar, Dict

from .table import Table


__all__ = ["Database"]

T = TypeVar("T")


class Database(metaclass=abc.ABCMeta):
    """Manage all the tables"""

    def __init__(self) -> None:
        self.tables: Dict[str, Table] = {}

        for name, table in self.__annotations__.items():
            obj = table(name)

            setattr(self, name, obj)

            self.add_table(obj)

        if not len(self.tables):
            raise ValueError("No tables defined")

    def add_table(self, table: Table) -> None:
        """Add a table to the database"""
        self.tables[table.name] = table

    def get_table(self, name: str) -> Table:
        """Get table by name"""
        return self.tables[name]
