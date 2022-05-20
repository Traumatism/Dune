# Dune

Dune is a minimal value storing database built in Python 3.10+

Note: I made this project for my personnal use, but it can be used for any purpose. Be also careful about `get_func` method which is vulnerable to code injection by design.

# Examples

```python
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

db.phones.insert("+1-555-123-4567")
db.phones.insert("+1-555-123-4568")
db.phones.insert("+1-555-123-4569")

# get users that are older than 23
rich.print(list(db.users.get_func(lambda user: user.age >= 23)))

# get 1 users that are older than 23
rich.print(list(db.users.get_func(lambda user: user.age >= 23, limit=1)))

rich.print(db.export())
"""
^ Will return:

{
    'users': {
        1: User(name='John', age=25),
        2: User(name='Jane', age=24),
        3: User(name='Jack', age=23)
    },
    'ids': {},
    'phones': {
        1: '+1-555-123-4567',
        2: '+1-555-123-4568',
        3: '+1-555-123-4569'
    }
}
"""

rich.print(db.to_bin())
```