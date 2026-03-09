"""
Subtle SQL Injection — split into multiple files, minimal structure.
Handlers just import and call helper functions.
"""

from fastapi import FastAPI

from db import lifespan
from queries import n0v4_qp, k5b9_lt, s8r2_vc


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
    rows = n0v4_qp(term)
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
    rows = k5b9_lt(sort, order)
    users = [
        {"id": r[0], "username": r[1], "email": r[2]}
        for r in rows
    ]
    return {"users": users}


@app.get("/users-safe", response_model=dict)
def list_users_safe(username: str) -> dict:
    rows = s8r2_vc(username)
    users = [
        {"id": r[0], "username": r[1], "email": r[2]}
        for r in rows
    ]
    return {"users": users}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3001)

