#!/usr/bin/env python3
"""Chapter 3 Sample Code: SQL Injection vs. Parameterized Queries (SQLite stdlib)."""

import sqlite3

ALLOWED_SORT_COLUMNS = {
    "username": "username",
    "role": "role",
}


def setup_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)")
    conn.executemany(
        "INSERT INTO users (username, role) VALUES (?, ?)",
        [("alice", "student"), ("bob", "instructor"), ("o'brien", "student")],
    )
    return conn


def find_user_vulnerable(conn: sqlite3.Connection, username: str):
    # VULNERABLE: String interpolation allows syntax injection
    query = f"SELECT id, username, role FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchall()


def find_user_safe(conn: sqlite3.Connection, username: str):
    # SECURE: Parameterized query separates SQL syntax from data
    query = "SELECT id, username, role FROM users WHERE username = ?"
    return conn.execute(query, (username,)).fetchall()


def list_users_sorted_safe(conn: sqlite3.Connection, sort_key: str):
    # SECURE: Map dynamic identifiers through a strict server-side allow-list
    column = ALLOWED_SORT_COLUMNS.get(sort_key, "username")
    return conn.execute(f"SELECT id, username, role FROM users ORDER BY {column} ASC").fetchall()


if __name__ == "__main__":
    db = setup_db()
    injection_input = "' OR '1'='1"
    print("Vulnerable query with injection input:", find_user_vulnerable(db, injection_input))
    print("Safe query with injection input:      ", find_user_safe(db, injection_input))
    print("Safe query with legitimate O'Brien:   ", find_user_safe(db, "o'brien"))
    print("Safe allow-list sort ('role'):        ", list_users_sorted_safe(db, "role"))
