# Pydantic schemas for request/response validation

# Import all schemas for easy access
# This allows importing like: from app.schemas import TodoCreate, UserCreate

from .todo import (
    PriorityLevel,
    TodoBase, 
    TodoCreate, 
    TodoUpdate, 
    TodoResponse
)

from .user import (
    UserBase,
    UserCreate,
    UserUpdate, 
    UserResponse,
    UserLogin,
    Token
)
