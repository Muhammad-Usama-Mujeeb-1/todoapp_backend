from typing import Optional
from enum import IntEnum, Enum
from pydantic import BaseModel, Field


class PriorityLevel(str, Enum):
    """Priority levels for todos"""
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

class TodoStatus(str, Enum):
    """Status levels for todos"""
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'


class TodoBase(BaseModel):
    """Base schema for Todo with common fields"""
    name: str = Field(
        ...,
        min_length=3, 
        description="Name of the todo",
        example="Learn FastAPI"
    )
    description: str = Field(
        ...,
        description="Description of the todo", 
        example="Study FastAPI documentation and build a todo app"
    )
    priority: PriorityLevel = Field(
        PriorityLevel.LOW, 
        description="Priority level of the todo", 
        example=PriorityLevel.HIGH
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
    name: Optional[str] = Field(
        None, 
        min_length=3, 
        description="Name of the todo", 
        example="Grocery Shopping"
    )
    description: Optional[str] = Field(
        None, 
        description="Description of the todo", 
        example="Buy vegetables and fruits"
    )
    priority: Optional[PriorityLevel] = Field(
        None, 
        description="Priority level of the todo", 
        example=PriorityLevel.MEDIUM
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
