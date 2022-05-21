# Dune

Dune is a minimal value storing database built in Python 3.10+

Note: I made this project for my personnal use, but it can be used for any purpose. Be also careful about `get_func` method which is 'vulnerable' to code injection by design.

# FastAPI example

```python
import fastapi
import uvicorn
import pydantic

from .database import Database
from .table import Table, TableStr


app = fastapi.FastAPI()


class User(pydantic.BaseModel):
    """User model"""

    name: str
    age: int


class MyDatabase(Database):
    """Database object"""

    users: Table[User] = Table("users")
    countries: TableStr = TableStr("countries")


@app.get("/")
def _():
    return {"message": "Welcome to DuneDB demo"}


@app.post("/users")
def _(name: str, age: int):
    """Add a new user"""
    MyDatabase.users.insert(User(name=name, age=age))
    return {}


@app.get("/users")
def _():
    """Get last 100 users"""
    return MyDatabase.users.get_func(lambda _: True, limit=100)


@app.get("/users/{key}")
def _(key: int):
    """Get a user"""
    return MyDatabase.users.get(key)


@app.delete("/users/{key}")
def _(key: int):
    """Delete a user"""
    MyDatabase.users.pop(key)
    return {}


@app.patch("/users/{key}")
def _(key: int, name: str, age: int):
    """Update a user"""
    MyDatabase.users.update(key, User(name=name, age=age))
    return {}


if __name__ == "__main__":
    uvicorn.run(
        "dune.__main__:app",
        host="127.0.0.1",
        port=2000,
        reload=True,
    )
```