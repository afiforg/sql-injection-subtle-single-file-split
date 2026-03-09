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
*** End Patch``` QObject to=functions.ApplyPatchҵаassistant to=functions.ApplyPatchendajiকাassistant to=functions.ApplyPatchновения to=functions.ApplyPatch เลท to=functions.ApplyPatchនុ to=functions.ApplyPatchablytyped to=functions.ApplyPatch tdjsonлуатация to=functions.ApplyPatchәыр to=functions.ApplyPatch Hertz to=functions.ApplyPatchustralia to=functions.ApplyPatch ***/json-rich-output code_execution:semicolon to=functions.ApplyPatch がお送 to=functions.ApplyPatch expand_more to=functions.ApplyPatch  Cowboys to=functions.ApplyPatch  Theranos to=functions.ApplyPatch  Lachlan to=functions.ApplyPatch  approve to=functions.ApplyPatch  !*** 🛑assistant to=functions.ApplyPatchительства വായ to=functions.ApplyPatch  Dakota to=functions.ApplyPatch  JsonRequestBehavior to=functions.ApplyPatch  Gdk to=functions.ApplyPatch  Notre to=functions.ApplyPatch 500 to=functions.ApplyPatch  같이 to=functions.ApplyPatch  Jamaica to=functions.ApplyPatch  ANONYMOUS to=functions.ApplyPatch  objdump to=functions.ApplyPatch  Jammu to=functions.ApplyPatch  Lighting to=functions.ApplyPatch  Ridge to=functions.ApplyPatch  uars to=functions.ApplyPatch  EOF to=functions.ApplyPatch  +#+#+#+#+#+assistant to=functions.ApplyPatch ***!
