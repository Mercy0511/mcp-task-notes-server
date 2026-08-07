"""
MCP Task and Notes Server

Provides tools for:
- Tasks management
- Notes management

Storage:
- SQLite Database
"""

from typing import Optional

from mcp.server.fastmcp import FastMCP

import database


# ============================================================
# MCP SERVER
# ============================================================

mcp = FastMCP("task-notes-server")


# Initialize Database

database.init_db()


# ============================================================
# TASK TOOLS
# ============================================================


@mcp.tool()
def add_task(
    title: str,
    due_date: Optional[str] = None,
    priority: str = "medium",
) -> dict:
    """
    Add a new task.

    Args:
        title: Task title
        due_date: Optional date YYYY-MM-DD
        priority: low, medium, high
    """

    if priority not in ("low", "medium", "high"):
        priority = "medium"

    return database.add_task(
        title,
        due_date,
        priority
    )



@mcp.tool()
def list_tasks(
    filter_by: str = "all"
) -> list[dict]:
    """
    List tasks.

    filter_by:
    - all
    - pending
    - completed
    - overdue
    """

    if filter_by not in (
        "all",
        "pending",
        "completed",
        "overdue"
    ):
        filter_by = "all"


    return database.list_tasks(
        filter_by
    )



@mcp.tool()
def complete_task(
    task_id: int
) -> dict:
    """
    Complete a task.
    """

    result = database.complete_task(
        task_id
    )


    if result is None:
        return {
            "error": f"Task {task_id} not found"
        }


    return result



@mcp.tool()
def delete_task(
    task_id: int
) -> dict:
    """
    Delete a task.
    """

    result = database.delete_task(
        task_id
    )


    return {
        "deleted": result,
        "task_id": task_id
    }



@mcp.tool()
def search_tasks(
    query: str
) -> list[dict]:
    """
    Search tasks.
    """

    return database.search_tasks(
        query
    )



# ============================================================
# NOTE TOOLS
# ============================================================


@mcp.tool()
def add_note(
    title: str,
    content: str,
    tags: Optional[str] = None,
) -> dict:
    """
    Add a note.
    """

    return database.add_note(
        title,
        content,
        tags
    )



@mcp.tool()
def list_notes() -> list[dict]:
    """
    List all notes.
    """

    return database.list_notes()



@mcp.tool()
def search_notes(
    query: str
) -> list[dict]:
    """
    Search notes.
    """

    return database.search_notes(
        query
    )



@mcp.tool()
def delete_note(
    note_id: int
) -> dict:
    """
    Delete a note.
    """

    result = database.delete_note(
        note_id
    )


    return {
        "deleted": result,
        "note_id": note_id
    }



# ============================================================
# RESOURCE
# ============================================================


@mcp.resource("summary://daily")
def daily_summary() -> str:
    """
    Daily task summary.
    """

    pending = database.list_tasks(
        "pending"
    )

    overdue = database.list_tasks(
        "overdue"
    )


    lines = []

    lines.append(
        f"Pending tasks: {len(pending)}"
    )


    lines.append(
        f"Overdue tasks: {len(overdue)}"
    )


    if pending:

        lines.append("\nUpcoming Tasks:")

        for task in pending[:5]:

            lines.append(
                f"- {task['title']} "
                f"[{task['priority']}]"
            )


    return "\n".join(lines)



# ============================================================
# MAIN
# ============================================================


if __name__ == "__main__":

    print("Database initialized")

    print(
        "Starting Task Notes MCP Server..."
    )

    mcp.run()