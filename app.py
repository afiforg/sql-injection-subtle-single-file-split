"""
Subtle SQL Injection — split into multiple files, minimal structure.
Handlers just import and call helper functions.
"""

from fastapi import FastAPI

from db import lifespan
from queries import find_by_username, find_with_sort, safe_find_by_username


app = FastAPI(
    title="Subtle SQL Injection (split, simple handlers)",
    lifespan=lifespan,
)


@app.get("/")
def root() -> dict:
    return {
        "message": "Subtle SQL injection API (split, simple handlers)",
        "endpoints": [
            "GET /users/search?q= or ?username=",
            "GET /users?sort=&order=",
            "GET /users-safe?username=",
        ],
    }


@app.get("/users/search", response_model=dict)
def search(
    q: str | None = None,
    username: str | None = None,
) -> dict:
    term = q or username or ""
    rows = find_by_username(term)
    users = [
        {"id": r[0], "username": r[1], "email": r[2]}
        for r in rows
    ]
    return {"users": users}


@app.get("/users", response_model=dict)
def list_users(
    sort: str = "id",
    order: str = "asc",
) -> dict:
    rows = find_with_sort(sort, order)
    users = [
        {"id": r[0], "username": r[1], "email": r[2]}
        for r in rows
    ]
    return {"users": users}


@app.get("/users-safe", response_model=dict)
def list_users_safe(username: str) -> dict:
    rows = safe_find_by_username(username)
    users = [
        {"id": r[0], "username": r[1], "email": r[2]}
        for r in rows
    ]
    return {"users": users}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3001)

