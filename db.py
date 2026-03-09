"""
Database connection and schema setup for the split-version demo.
No request/handler logic here.
"""

import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI


DB_PATH = Path(__file__).resolve().parent / "data.db"
_conn: sqlite3.Connection | None = None


def init_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        INSERT OR IGNORE INTO users (id, username, email) VALUES
        (1, 'admin', 'admin@example.com'),
        (2, 'alice', 'alice@example.com'),
        (3, 'bob', 'bob@example.com')
        """
    )
    conn.commit()


def get_conn() -> sqlite3.Connection:
    if _conn is None:
        raise RuntimeError("Database connection is not initialized")
    return _conn


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _conn
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    init_schema(conn)
    _conn = conn
    try:
        yield
    finally:
        conn.close()
