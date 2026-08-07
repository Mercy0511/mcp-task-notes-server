"""
Database layer for the Task & Notes MCP Server.
Handles all SQLite operations.
"""

import sqlite3
from pathlib import Path
from typing import Any, Optional


# Current project folder
BASE_DIR = Path(__file__).parent

# Database file
DB_PATH = BASE_DIR / "tasks_notes.db"

# Schema file
SCHEMA_PATH = BASE_DIR / "schema.sql"


def get_connection() -> sqlite3.Connection:
    """Create SQLite connection with row access by column name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create tables during server startup."""

    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(
            f"schema.sql not found at: {SCHEMA_PATH}"
        )

    with get_connection() as conn:
        conn.executescript(SCHEMA_PATH.read_text())


def row_to_dict(row: sqlite3.Row) -> Optional[dict]:
    return dict(row) if row else None


# ---------------- TASKS ----------------


def add_task(
    title: str,
    due_date: Optional[str] = None,
    priority: str = "medium"
) -> dict:

    with get_connection() as conn:
        cur = conn.execute(
            """
            INSERT INTO tasks 
            (title, due_date, priority)
            VALUES (?, ?, ?)
            """,
            (title, due_date, priority)
        )

        conn.commit()

        return get_task(cur.lastrowid)


def get_task(task_id: int) -> Optional[dict]:

    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM tasks WHERE id=?",
            (task_id,)
        ).fetchone()

        return row_to_dict(row)


def list_tasks(filter_by: str = "all") -> list[dict]:

    query = "SELECT * FROM tasks"
    params = ()

    if filter_by == "pending":
        query += " WHERE status='pending'"

    elif filter_by == "completed":
        query += " WHERE status='completed'"

    elif filter_by == "overdue":
        query += """
        WHERE status='pending'
        AND due_date IS NOT NULL
        AND due_date < date('now')
        """


    query += """
    ORDER BY
    CASE priority
        WHEN 'high' THEN 1
        WHEN 'medium' THEN 2
        ELSE 3
    END,
    due_date ASC
    """


    with get_connection() as conn:

        rows = conn.execute(
            query,
            params
        ).fetchall()

        return [
            row_to_dict(row)
            for row in rows
        ]


def complete_task(task_id: int) -> Optional[dict]:

    with get_connection() as conn:

        conn.execute(
            """
            UPDATE tasks
            SET status='completed',
            completed_at=datetime('now')
            WHERE id=?
            """,
            (task_id,)
        )

        conn.commit()

        return get_task(task_id)



def delete_task(task_id: int) -> bool:

    with get_connection() as conn:

        cur = conn.execute(
            "DELETE FROM tasks WHERE id=?",
            (task_id,)
        )

        conn.commit()

        return cur.rowcount > 0



def search_tasks(query: str) -> list[dict]:

    with get_connection() as conn:

        rows = conn.execute(
            """
            SELECT * FROM tasks
            WHERE title LIKE ?
            ORDER BY created_at DESC
            """,
            (f"%{query}%",)
        ).fetchall()


        return [
            row_to_dict(row)
            for row in rows
        ]



# ---------------- NOTES ----------------


def add_note(
    title: str,
    content: str,
    tags: Optional[str] = None
) -> dict:

    with get_connection() as conn:

        cur = conn.execute(
            """
            INSERT INTO notes
            (title, content, tags)
            VALUES (?, ?, ?)
            """,
            (title, content, tags)
        )

        conn.commit()

        return get_note(cur.lastrowid)



def get_note(note_id: int) -> Optional[dict]:

    with get_connection() as conn:

        row = conn.execute(
            "SELECT * FROM notes WHERE id=?",
            (note_id,)
        ).fetchone()

        return row_to_dict(row)



def list_notes() -> list[dict]:

    with get_connection() as conn:

        rows = conn.execute(
            """
            SELECT * FROM notes
            ORDER BY updated_at DESC
            """
        ).fetchall()


        return [
            row_to_dict(row)
            for row in rows
        ]



def search_notes(query: str) -> list[dict]:

    with get_connection() as conn:

        rows = conn.execute(
            """
            SELECT * FROM notes
            WHERE title LIKE ?
            OR content LIKE ?
            OR tags LIKE ?
            ORDER BY updated_at DESC
            """,
            (
                f"%{query}%",
                f"%{query}%",
                f"%{query}%"
            )
        ).fetchall()


        return [
            row_to_dict(row)
            for row in rows
        ]



def delete_note(note_id: int) -> bool:

    with get_connection() as conn:

        cur = conn.execute(
            "DELETE FROM notes WHERE id=?",
            (note_id,)
        )

        conn.commit()

        return cur.rowcount > 0
