# Todo API endpoints - organized from your existing main.py code
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional

# Import your schemas
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse, PriorityLevel

# TODO: Replace this with database operations when you integrate MongoDB
# For now, keeping your existing in-memory storage for learning
all_todos = [
    TodoResponse(todo_id=1, todo_name='Sports', todo_description='Go to the gym', priority=PriorityLevel.HIGH),
    TodoResponse(todo_id=2, todo_name='Study', todo_description='Read FastAPI documentation', priority=PriorityLevel.MEDIUM),
    TodoResponse(todo_id=3, todo_name='Grocery', todo_description='Buy vegetables and fruits', priority=PriorityLevel.LOW),
    TodoResponse(todo_id=4, todo_name='Work', todo_description='Finish the project report', priority=PriorityLevel.HIGH),
    TodoResponse(todo_id=5, todo_name='Relax', todo_description='Watch a movie', priority=PriorityLevel.MEDIUM),
    TodoResponse(todo_id=6, todo_name='Travel', todo_description='Plan a weekend trip', priority=PriorityLevel.LOW),
    TodoResponse(todo_id=7, todo_name='Cooking', todo_description='Try a new recipe', priority=PriorityLevel.LOW),
    TodoResponse(todo_id=8, todo_name='Reading', todo_description='Read a new book', priority=PriorityLevel.LOW),
    TodoResponse(todo_id=9, todo_name='Cleaning', todo_description='Clean the house', priority=PriorityLevel.LOW),
    TodoResponse(todo_id=10, todo_name='Meditation', todo_description='Practice mindfulness', priority=PriorityLevel.LOW),
]

router = APIRouter()


@router.get('/', response_model=List[TodoResponse])
def get_todos(firstn: Optional[int] = None):
    """
    Get all todos or first N todos
    
    - **firstn**: Optional parameter to limit number of todos returned
    """
    if firstn:
        return all_todos[:firstn]
    return all_todos


@router.get('/{todo_id}', response_model=TodoResponse)
def get_todo(todo_id: int):
    """
    Get a specific todo by ID
    
    - **todo_id**: The ID of the todo to retrieve
    """
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@router.post('/', response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    """
    Create a new todo
    
    - **todo**: Todo data (name, description, priority)
    """
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1

    new_todo = TodoResponse(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority
    )

    all_todos.append(new_todo)
    return new_todo


@router.put('/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    """
    Update an existing todo
    
    - **todo_id**: The ID of the todo to update
    - **updated_todo**: Updated todo data (all fields optional)
    """
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete('/{todo_id}', response_model=TodoResponse)
def delete_todo(todo_id: int):
    """
    Delete a todo by ID
    
    - **todo_id**: The ID of the todo to delete
    """
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail="Todo not found")