#!/usr/bin/python3
"""Todo database configuration settings."""
from motor import motor_asyncio
from farm_todo.backend.models.todos import Todo

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collections = database.todo


async def fetch_one_todo(title: str):
    """Fetch one todo by title."""
    document = await collections.find_one({"title": title})
    return document


async def fetch_all_todos() -> list:
    """Fetch all todos."""
    todos = []
    cursor = collections.find({})

    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    """Create todo."""
    document = todo
    await collections.insert_one(document)
    return document


async def update_todo(title: str, desc: str):
    """Update a todo by title."""
    await collections.update_one(
        {"title": title}, {"$set": {"description": desc}}
    )
    result = await collections.find_one({"title": title})
    return result


async def remove_todo(title: str):
    """Delete a todo by title."""
    await collections.delete_one({"title": title})
    return True
