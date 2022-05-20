import rich
import typing

from dune.table import Table
from dune.database import Database


class User(typing.NamedTuple):
    """User object"""

    name: str
    age: int


class MyDB(Database):
    """MyDB is a database"""

    users: Table[User] = Table("users")  # table that stores User objects
    ids: Table[int] = Table("ids")  # table that stores ints
    phones: Table[str] = Table("phones")  # table that stores strings


db = MyDB()

db.users.insert(User("John", 25))
db.users.insert(User("Jane", 24))
db.users.insert(User("Jack", 23))

# get users that are older than 23
rich.print(list(db.users.get_func(lambda user: user.age >= 23)))

# get 1 users that are older than 23
rich.print(list(db.users.get_func(lambda user: user.age >= 23, limit=1)))

rich.print(db.export())
rich.print(db.to_bin())
