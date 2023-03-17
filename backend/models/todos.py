#!/usr/bin/python3
"""Todos model."""
from pydantic import BaseModel


class Todo(BaseModel):
    """Todo model.

    Args:
        title (str): title of the todo
        description (str): description of the todo
    """

    title: str
    description: str


class TodoUpdate(BaseModel):
    """TodoUpdate model.

    Args:
        description (str): description of the todo
    """

    description: str
