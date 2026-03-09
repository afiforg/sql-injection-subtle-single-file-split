"""
Query helpers and data access functions for the split-version demo.
Contains both vulnerable and safe variants for testing.
"""

from typing import List, Sequence

from .db import get_conn


def _zqf1_hh(column_in: str, value_in: str) -> str:
    if not value_in:
        return "1=1"
    return f"{column_in} = '{value_in}'"


def _mk7r_po(column_in: str, direction_in: str) -> str:
    d = "DESC" if direction_in and direction_in.upper() == "DESC" else "ASC"
    return f"ORDER BY {column_in} {d}"


def _u1x_rows(rows_in: Sequence[Sequence[object]]) -> List[tuple]:
    # Keep the projection logic here so handlers only see simple tuples
    result_list: List[tuple] = []
    for row in rows_in:
        a0, a1, a2 = row[0], row[1], row[2]
        result_list.append((a0, a1, a2))
    return result_list


def n0v4_qp(user_in: str) -> List[tuple]:
    conn = get_conn()
    cond = _zqf1_hh("username", user_in)
    query = f"SELECT id, username, email FROM users WHERE {cond}"
    result = conn.execute(query)
    rows = result.fetchall()
    return _u1x_rows(rows)


def k5b9_lt(sort_in: str, dir_in: str) -> List[tuple]:
    conn = get_conn()
    order_clause = _mk7r_po(sort_in, dir_in)
    query = f"SELECT id, username, email FROM users {order_clause}"
    result = conn.execute(query)
    rows = result.fetchall()
    return _u1x_rows(rows)


def s8r2_vc(user_in: str) -> List[tuple]:
    conn = get_conn()
    query = "SELECT id, username, email FROM users WHERE username = ?"
    result = conn.execute(query, (user_in,))
    rows = result.fetchall()
    return _u1x_rows(rows)

