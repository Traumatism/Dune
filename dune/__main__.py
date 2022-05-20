import rich
import typing

from .table import Table
from .database import Database


class User(typing.NamedTuple):
    """User object"""

    name: str
    age: int


db = Database()

users: Table[User] = Table("users")

users.insert(User("John", 25))
users.insert(User("Jane", 24))
users.insert(User("Jack", 23))

db.add_table(users)

rich.print(list(users.get_func(lambda user: user.age >= 23)))

rich.print(list(users.get_func(lambda user: user.age >= 23, limit=1)))

rich.print(db.export())

rich.print(db.to_bin())
