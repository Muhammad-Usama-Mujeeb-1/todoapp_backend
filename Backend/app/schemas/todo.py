from typing import Optional
from enum import IntEnum, Enum
from pydantic import BaseModel, Field


class PriorityLevel(IntEnum):
    """Priority levels for todos"""
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class TodoStatus(str, Enum):
    """Status levels for todos"""
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


class TodoBase(BaseModel):
    """Base schema for Todo with common fields"""
    todo_name: str = Field(
        ...,
        min_length=3, 
        description="Name of the todo",
        example="Learn FastAPI"
    )
    todo_description: str = Field(
        ...,
        description="Description of the todo", 
        example="Study FastAPI documentation and build a todo app"
    )
    priority: PriorityLevel = Field(
        PriorityLevel.LOW, 
        description="Priority level of the todo", 
        example=3
    )
    status: TodoStatus = Field(
        TodoStatus.NOT_STARTED, 
        description="Status of the todo", 
        example=TodoStatus.NOT_STARTED
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
        description="Priority level of the todo", 
        example=1
    )
    status: Optional[TodoStatus] = Field(
        None, 
        description="Status of the todo", 
        example=TodoStatus.IN_PROGRESS
    )


class TodoResponse(TodoBase):
    """Schema for todo response with MongoDB ObjectId as string"""
    id: str = Field(
        ..., 
        description="Unique identifier for the todo (MongoDB ObjectId as string)", 
        example="507f1f77bcf86cd799439011"
    )

    class Config:
        from_attributes = True