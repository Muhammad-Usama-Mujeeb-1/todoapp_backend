# Todo Pydantic schemas for request/response validation
from typing import Optional
from enum import IntEnum
from pydantic import BaseModel, Field


class PriorityLevel(IntEnum):
    """Priority levels for todos"""
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class TodoBase(BaseModel):
    """Base schema for Todo with common fields"""
    todo_name: str = Field(
        ..., 
        min_length=3, 
        description="Name of the todo", 
        example="Grocery Shopping"
    )
    todo_description: str = Field(
        ..., 
        description="Description of the todo", 
        example="Buy vegetables and fruits"
    )
    priority: PriorityLevel = Field(
        PriorityLevel.LOW, 
        description='Priority level of the todo', 
        example=1
    )


class TodoCreate(TodoBase):
    """Schema for creating a new todo"""
    pass


class TodoUpdate(BaseModel):
    """Schema for updating an existing todo"""
    todo_name: Optional[str] = Field(
        None, 
        min_length=3, 
        description="Name of the todo", 
        example="Grocery Shopping"
    )
    todo_description: Optional[str] = Field(
        None, 
        description="Description of the todo", 
        example="Buy vegetables and fruits"
    )
    priority: Optional[PriorityLevel] = Field(
        None, 
        description='Priority level of the todo', 
        example=1
    )


class TodoResponse(TodoBase):
    """Schema for todo response with ID"""
    todo_id: int = Field(
        ..., 
        description="Unique identifier for the todo", 
        example=1
    )

    class Config:
        from_attributes = True