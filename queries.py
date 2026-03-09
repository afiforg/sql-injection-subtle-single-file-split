"""
Query helpers and data access functions for the split-version demo.
Contains both vulnerable and safe variants for testing.
"""

from typing import List, Sequence

from .db import get_conn


def build_condition(column: str, value: str) -> str:
    if not value:
        return "1=1"
    return f"{column} = '{value}'"


def order_by(column: str, direction: str) -> str:
    d = "DESC" if direction and direction.upper() == "DESC" else "ASC"
    return f"ORDER BY {column} {d}"


def _rows_to_tuples(rows: Sequence[Sequence[object]]) -> List[tuple]:
    # Keep the projection logic here so handlers only see simple tuples
    result: List[tuple] = []
    for row in rows:
        result.append((row[0], row[1], row[2]))
    return result


def find_by_username(username: str) -> List[tuple]:
    conn = get_conn()
    cond = build_condition("username", username)
    query = f"SELECT id, username, email FROM users WHERE {cond}"
    result = conn.execute(query)
    rows = result.fetchall()
    return _rows_to_tuples(rows)


def find_with_sort(sort_column: str, sort_dir: str) -> List[tuple]:
    conn = get_conn()
    order_clause = order_by(sort_column, sort_dir)
    query = f"SELECT id, username, email FROM users {order_clause}"
    result = conn.execute(query)
    rows = result.fetchall()
    return _rows_to_tuples(rows)


def safe_find_by_username(username: str) -> List[tuple]:
    conn = get_conn()
    query = "SELECT id, username, email FROM users WHERE username = ?"
    result = conn.execute(query, (username,))
    rows = result.fetchall()
    return _rows_to_tuples(rows)

