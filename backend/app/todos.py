#!/usr/bin/python3
"""Todos module."""
from fastapi import APIRouter, HTTPException, status
from farm_todo.backend.database.db_connect import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)
from farm_todo.backend.models.todos import Todo, TodoUpdate

todos_router = APIRouter(prefix="/api/todos", tags=["Todos",])


@todos_router.get("/")
async def get_todos() -> list:
    """Retrieve a list of all available todos."""
    response = await fetch_all_todos()
    return response


@todos_router.get("/{todo_title}", response_model=Todo)
async def get_todos_by_title(todo_title: str) -> dict:
    """Return a todo by given todo title."""
    response = await fetch_one_todo(todo_title)
    if response:
        return response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with '{todo_title}' not found."
    )


@todos_router.post("/create", response_model=Todo, status_code=201)
async def add_todo(todo: Todo) -> dict:
    """Create a todo."""
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Bad request!"
    )


@todos_router.put(
    "/edit/{todo_title}", response_model=Todo, status_code=201
)
async def edit_todo(todo_title: str, desc: TodoUpdate) -> dict:
    """Edit a todo."""
    desc = desc.dict()["description"]
    response = await update_todo(todo_title, desc)
    if response:
        return response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with '{todo_title}' not found."
    )


@todos_router.delete("/delete/{todo_title")
async def delete_todo(todo_title: str) -> str:
    """Remove a todo by given title."""
    response = await remove_todo(todo_title)
    if response:
        return "Todo delete successfully."
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with '{todo_title}' not found."
    )
