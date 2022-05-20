# Dune

Dune is a minimal value storing database built in Python 3.10+

Note: I made this project for my personnal use, but it can be used for any purpose. Be also careful about `get_func` method which is vulnerable to code injection by design.

# Examples

```python
import rich
import typing

from .table import Table
from .database import Database


class User(typing.NamedTuple):
    """User object"""

    name: str
    age: int


db = Database()

# create a table that accept User objects
users: Table[User] = Table("users")

users.insert(User("John", 25))
users.insert(User("Jane", 24))
users.insert(User("Jack", 23))

db.add_table(users)

# get users that are older than 23
rich.print(list(users.get_func(lambda user: user.age >= 23)))

# get the last user who is older than 23
rich.print(list(users.get_func(lambda user: user.age >= 23, limit=1)))

# get the user with the ID (2)
rich.print(users.get(2))

# export the database to JSON
rich.print(db.export())

# export the database to bytes zlib(pickle(content))
rich.print(db.to_bin())
```