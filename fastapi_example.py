import os
import pickle
import fastapi
import uvicorn
import pydantic

from dune.database import Database
from dune.table import Table, TableStr

app = fastapi.FastAPI()

__all__ = ["MyDatabase"]


class User(pydantic.BaseModel):
    """User model"""

    name: str
    age: int


class MyDatabase(Database):
    """Database object"""

    users: Table[User]
    countries: TableStr


if os.path.exists("backup.dune"):
    db = pickle.load(open("backup.dune", "rb"))
else:
    db = MyDatabase()


@app.get("/")
def _():
    return {"message": "Welcome to DuneDB demo"}


@app.post("/users")
def _(name: str, age: int):
    """Add a new user"""
    return {"key": db.users.insert(User(name=name, age=age))}


@app.get("/users")
def _():
    """Get last 100 users"""
    return db.users.get_func(lambda _: True, limit=100)


@app.get("/users/search")
def _(query: str):
    """Get users by name"""
    return db.users.get_func(lambda user: query in user.name)


@app.get("/users/{key}")
def _(key: int):
    """Get a user"""
    return db.users.get(key)


@app.delete("/users/{key}")
def _(key: int):
    """Delete a user"""
    db.users.pop(key)
    return {}


@app.patch("/users/{key}")
def _(key: int, name: str, age: int):
    """Update a user"""
    db.users.update(key, User(name=name, age=age))
    return {}


@app.get("/export")
def _():
    """Export database"""
    print("exporting...")
    with open("backup.dune", "wb") as f:
        pickle.dump(db, f)


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_example:app",
        host="127.0.0.1",
        port=2000,
        reload=True,
    )
