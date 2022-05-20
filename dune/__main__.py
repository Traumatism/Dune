import rich
import typing

from dune.table import Table, TableStr
from dune.database import Database


class User(typing.NamedTuple):
    """User object"""

    name: str
    age: int


class MyDB(Database):
    """MyDB is a database"""

    users: Table[User] = Table("users")  # table that stores User objects
    ids: Table[int] = Table("ids")  # table that stores ints

    phones: TableStr[str] = TableStr("phones")  # table that stores strings
    names: TableStr[str] = TableStr("names")  # table that stores strings


db = MyDB()

db.users.insert(User("John", 25))
db.users.insert(User("Jane", 24))
db.users.insert(User("Jack", 23))

db.phones.insert("+1-555-123-4567")
db.phones.insert("+1-555-123-4568")
db.phones.insert("+1-555-123-4569")

db.names.insert("John")
db.names.insert("Jenny")
db.names.insert("Viktor")
db.names.insert("Penny")
db.names.insert("Jake")
db.names.insert("Victor")
db.names.insert("Jane")
db.names.insert("Jack")

rich.print(list(db.names.search("Vi")))

# get users that are older than 23
rich.print(list(db.users.get_func(lambda user: user.age >= 23)))

# get 1 users that are older than 23
rich.print(list(db.users.get_func(lambda user: user.age >= 23, limit=1)))

rich.print(db.export())
rich.print(db.to_bin())
