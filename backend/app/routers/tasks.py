from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: str = "todo"  # todo, in_progress, done
    due_date: Optional[datetime] = None
    source: str = "user"

tasks_db: List[Task] = []
task_id_counter = 1

@router.get("/")
def get_tasks(status: Optional[str] = None):
    """Get all tasks, optionally filtered by status"""
    if status:
        return [t for t in tasks_db if t.status == status]
    return tasks_db

@router.post("/")
def create_task(task: Task):
    """Create a new task"""
    global task_id_counter
    task.id = task_id_counter
    task_id_counter += 1
    tasks_db.append(task)
    return task

@router.patch("/{task_id}")
def update_task(task_id: int, task_update: dict):
    """Update a task"""
    for task in tasks_db:
        if task.id == task_id:
            for key, value in task_update.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    """Delete a task"""
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return {"status": "deleted"}
