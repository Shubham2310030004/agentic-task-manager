# Agentic AI Task Manager

## Overview

An intelligent task management system powered by LLMs with vector-based memory for long-term context retention. Features include conversational task creation, automatic memory indexing, and API integrations for weather, calendar, and email.

## Features

- **LLM-Powered Agent**: Conversational interface for task management
- **Vector-Based Memory**: Persistent, searchable memory using embeddings
- **Task Management**: Create, update, delete, and filter tasks
- **CRUD Endpoints**: Full REST API for task operations
- **Memory Recall**: Smart memory retrieval based on semantic similarity
- **Extensible**: Ready for weather, calendar, and email API integrations

## Project Structure

```
agentic-task-manager/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application
│   │   ├── __init__.py
│   │   └── routers/
│   │       ├── tasks.py             # Task CRUD endpoints
│   │       ├── agent.py             # LLM agent endpoints
│   │       └── __init__.py
│   ├── requirements.txt             # Python dependencies
├── frontend/                        # React + Vite (to be added)
├── docker-compose.yml               # Docker orchestration
├── .gitignore
└── README.md
```

## Installation

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/Shubham2310030004/agentic-task-manager.git
cd agentic-task-manager
```

2. Create virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Tasks
- `GET /api/tasks` - List all tasks (with optional status filter)
- `POST /api/tasks` - Create a new task
- `PATCH /api/tasks/{id}` - Update a task
- `DELETE /api/tasks/{id}` - Delete a task

### Agent
- `POST /api/agent/chat` - Send message to LLM task assistant
- `POST /api/agent/remember` - Store a memory
- `GET /api/agent/memories/{user_id}` - Retrieve user memories

## Task Schema

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Optional task description",
  "status": "todo",  // todo, in_progress, done
  "due_date": "2024-12-31T23:59:59",
  "source": "user"   // user, email, calendar, weather_alert
}
```

## Next Steps

- [ ] Add LLM client integration (OpenAI, local LLMs)
- [ ] Implement vector memory store (FAISS, Chroma, Pinecone)
- [ ] Create React frontend dashboard
- [ ] Add weather API integration
- [ ] Add calendar API integration
- [ ] Add email automation
- [ ] Database integration (PostgreSQL)
- [ ] Docker containerization
- [ ] Unit tests and CI/CD

## Technologies

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **LLM**: OpenAI API (configurable)
- **Memory**: Vector embeddings with in-memory storage
- **Frontend**: React + Vite + TypeScript (planned)
- **Database**: SQLite (development), PostgreSQL (production)

## Environment Variables

Create a `.env` file in the backend folder:

```env
OPENAI_API_KEY=your_key_here
DATABASE_URL=sqlite:///./tasks.db
AGENT_MODEL=gpt-4
```

## License

MIT

## Author

Shubham (2310030004)
