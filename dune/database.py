import abc

from typing import TypeVar, Dict, Union

from .table import Table


__all__ = ["Database"]

T = TypeVar("T")


class Database(metaclass=abc.ABCMeta):
    """Manage all the tables"""

    def __init__(self) -> None:
        self.__tables: Dict[str, Table] = {}

        map(
            lambda t: self.add_table(t[1](t[0])),
            self.__annotations__.items(),
        )

        if not len(self.tables):
            raise ValueError("No tables defined")

    @property
    def tables(self) -> Dict[str, Table]:
        """Get all tables"""
        return self.__tables

    def add_table(self, table: Table) -> None:
        """Add a table to the database"""
        setattr(self, table.name, table)
        self.__tables[table.name] = table

    def get_table(self, name: str) -> Union[Table, int]:
        """Get table by name"""
        return self.tables.get(name, -1)
