# Todo API endpoints - organized from your existing main.py code
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional

# Import your schemas
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse, PriorityLevel, TodoStatus

# TODO: Replace this with database operations when you integrate MongoDB
# For now, using string IDs (simulating MongoDB ObjectIds) for learning
all_todos = [
    TodoResponse(id="507f1f77bcf86cd799439011", todo_name='Sports', todo_description='Go to the gym', priority=PriorityLevel.HIGH, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd799439012", todo_name='Study', todo_description='Read FastAPI documentation', priority=PriorityLevel.MEDIUM, status=TodoStatus.IN_PROGRESS),
    TodoResponse(id="507f1f77bcf86cd799439013", todo_name='Grocery', todo_description='Buy vegetables and fruits', priority=PriorityLevel.LOW, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd799439014", todo_name='Work', todo_description='Finish the project report', priority=PriorityLevel.HIGH, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd799439015", todo_name='Relax', todo_description='Watch a movie', priority=PriorityLevel.MEDIUM, status=TodoStatus.COMPLETED),
    TodoResponse(id="507f1f77bcf86cd799439016", todo_name='Travel', todo_description='Plan a weekend trip', priority=PriorityLevel.LOW, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd799439017", todo_name='Cooking', todo_description='Try a new recipe', priority=PriorityLevel.LOW, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd799439018", todo_name='Reading', todo_description='Read a new book', priority=PriorityLevel.LOW, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd799439019", todo_name='Cleaning', todo_description='Clean the house', priority=PriorityLevel.LOW, status=TodoStatus.NOT_STARTED),
    TodoResponse(id="507f1f77bcf86cd79943901a", todo_name='Meditation', todo_description='Practice mindfulness', priority=PriorityLevel.LOW, status=TodoStatus.NOT_STARTED),
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
def get_todo(todo_id: ObjectId):
    """
    Get a specific todo by ID
    
    - **todo_id**: The ID of the todo to retrieve (MongoDB ObjectId string)
    """
    for todo in all_todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@router.post('/', response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    """
    Create a new todo
    
    - **todo**: Todo data (only name and description required)
    - **priority**: Optional - defaults to LOW if not provided
    - **status**: Optional - defaults to NOT_STARTED if not provided
    """
    # Generate a new ObjectId-like string (in real MongoDB, this would be generated automatically)
    import time
    new_todo_id = f"507f1f77bcf86cd{int(time.time()):x}"[:24]

    # Set defaults for optional fields
    priority = todo.priority if todo.priority is not None else PriorityLevel.LOW
    status = todo.status if todo.status is not None else TodoStatus.NOT_STARTED

    new_todo = TodoResponse(
        id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=priority,
        status=status
    )

    all_todos.append(new_todo)
    return new_todo


@router.put('/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id: ObjectId, updated_todo: TodoUpdate):
    """
    Update an existing todo
    
    - **todo_id**: The ID of the todo to update (MongoDB ObjectId string)
    - **updated_todo**: Updated todo data (all fields optional)
    """
    for todo in all_todos:
        if todo.id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            if updated_todo.status is not None:
                todo.status = updated_todo.status
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete('/{todo_id}', response_model=TodoResponse)
def delete_todo(todo_id: ObjectId):
    """
    Delete a todo by ID
    
    - **todo_id**: The ID of the todo to delete (MongoDB ObjectId string)
    """
    for index, todo in enumerate(all_todos):
        if todo.id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail="Todo not found")