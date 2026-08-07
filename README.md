<<<<<<< HEAD
# 🚀 MCP Task Notes Server

<p align="center">
  A production-style Model Context Protocol (MCP) server for AI-powered task and note management using Python and SQLite.
</p>

---

## 📌 Overview

**MCP Task Notes Server** is a lightweight local MCP server built using **Python FastMCP** that enables AI assistants to interact with task and note management tools through the **Model Context Protocol (MCP)**.

The server provides structured tools for creating, retrieving, updating, searching, and deleting tasks and notes while maintaining persistent data storage using SQLite.

This project demonstrates how modern AI applications can securely interact with custom backend services through MCP.

---

## ✨ Key Features

### 📋 Task Management

- Create new tasks
- Retrieve task lists
- Search tasks by keyword
- Mark tasks as completed
- Delete tasks
- Filter tasks based on status:
  - All
  - Pending
  - Completed
  - Overdue


### 📝 Note Management

- Create personal notes
- Retrieve saved notes
- Search notes
- Delete notes
- Support note tagging


### 🗄️ Data Persistence

- SQLite-based local storage
- Automatic database initialization
- Clean database abstraction layer
- Structured SQL schema management


### 🤖 MCP Integration

- Built with FastMCP framework
- Exposes reusable AI tools
- Compatible with MCP-enabled AI clients
- Designed for AI agent workflows

---

# 🏛️ Architecture

```
                 AI Application
                      |
                      |
              Model Context Protocol
                      |
                      |
              FastMCP Server Layer
                      |
        --------------------------------
        |                              |
     server.py                    database.py
        |                              |
        --------------------------------
                      |
                  SQLite Database
                      |
              tasks_notes.db
```

---

# 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Backend Development |
| FastMCP | MCP Server Framework |
| SQLite | Database Storage |
| SQL | Database Management |
| MCP Protocol | AI Tool Communication |

---

# 📂 Project Structure

```
mcp-task-notes-server/
│
├── server.py
│   └── MCP server implementation
│
├── database.py
│   └── SQLite database operations
│
├── schema.sql
│   └── Database table definitions
│
├── README.md
│
├── .gitignore
│
└── .venv/
    └── Python virtual environment
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/<username>/mcp-task-notes-server.git
```

Navigate into the project:

```bash
cd mcp-task-notes-server
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install mcp[cli]
```

---

# ▶️ Running the MCP Server

Start the server:

```bash
python server.py
```

Successful startup:

```
Database initialized
Starting Task Notes MCP Server...
```

---

# 🛠️ MCP Tools Available

## Task Tools

| Tool | Description |
|------|-------------|
| `add_task` | Create a new task |
| `list_tasks` | Retrieve tasks |
| `complete_task` | Update task status |
| `delete_task` | Remove a task |
| `search_tasks` | Search tasks |

---

## Note Tools

| Tool | Description |
|------|-------------|
| `add_note` | Create a note |
| `list_notes` | Retrieve notes |
| `search_notes` | Search notes |
| `delete_note` | Remove notes |

---

# 🔍 Testing with MCP Inspector

Install MCP CLI:

```bash
pip install mcp[cli]
```

Launch inspector:

```bash
mcp dev server.py
```

MCP Inspector allows testing:

- Available tools
- Tool inputs
- Tool responses
- Server communication

---

# 🗃️ Database Design

## Tasks Table

| Column | Description |
|--------|-------------|
| id | Unique identifier |
| title | Task title |
| due_date | Task deadline |
| priority | Task priority |
| status | Task status |
| completed_at | Completion timestamp |
| created_at | Creation timestamp |


## Notes Table

| Column | Description |
|--------|-------------|
| id | Unique identifier |
| title | Note title |
| content | Note details |
| tags | Note categories |
| updated_at | Last update timestamp |

---

# 🔐 Design Principles

- Separation of concerns
- Modular backend architecture
- Local-first data storage
- Reusable MCP tools
- Clean database abstraction

---

# 🚀 Future Enhancements

- REST API integration using FastAPI
- Web dashboard interface
- Authentication and authorization
- Cloud database migration
- Docker containerization
- AI-based task prioritization
- Notification and reminder system


---

# 🎓 Skills Demonstrated

Through this project:

✔ MCP Server Development  
✔ Python Backend Engineering  
✔ SQLite Database Management  
✔ AI Tool Integration  
✔ Software Architecture Design  
✔ API-Oriented Development  


---

# 👨‍💻 Author

**Mercy**

BCA Final Year Student

Interested in:

- Artificial Intelligence
- Python Development
- Backend Engineering
- MCP & AI Agent Systems


---
=======
# mcp-task-notes-server
>>>>>>> df0852c29a922ffcd2296d1d90263173064339f6
