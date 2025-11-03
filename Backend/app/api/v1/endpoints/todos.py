# Todo API endpoints with MongoDB CRUD operations
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

# Import schemas and CRUD operations
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse, PriorityLevel, TodoStatus
from app.crud.todo import todo_crud

router = APIRouter()


@router.get('/', response_model=List[TodoResponse])
async def get_todos(
    limit: int = Query(100, description="Maximum number of todos to return"),
    skip: int = Query(0, description="Number of todos to skip"),
    status: Optional[TodoStatus] = Query(None, description="Filter by status"),
    priority: Optional[PriorityLevel] = Query(None, description="Filter by priority")
):
    """
    Get all todos with optional filtering and pagination
    
    - **limit**: Maximum number of todos to return (default: 100)
    - **skip**: Number of todos to skip for pagination (default: 0)
    - **status**: Filter todos by status (optional)
    - **priority**: Filter todos by priority (optional)
    """
    try:
        todos = await todo_crud.get_todos(
            skip=skip,
            limit=limit,
            status_filter=status,
            priority_filter=priority
        )
        
        # Convert TodoModel to TodoResponse format
        response_todos = []
        for todo in todos:
            response_data = todo.to_response_dict()
            response_todos.append(TodoResponse(**response_data))
        
        return response_todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch todos: {str(e)}")


@router.get('/{todo_id}', response_model=TodoResponse)
async def get_todo(todo_id: str):
    """
    Get a specific todo by ID
    
    - **todo_id**: The ID of the todo to retrieve (MongoDB ObjectId string)
    """
    try:
        todo = await todo_crud.get_todo(todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        # Convert TodoModel to TodoResponse format
        response_data = todo.to_response_dict()
        return TodoResponse(**response_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch todo: {str(e)}")


@router.post('/', response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    """
    Create a new todo
    
    - **todo**: Todo data with name and description required, priority and status optional
    - **priority**: Defaults to LOW if not provided
    - **status**: Defaults to NOT_STARTED if not provided
    """
    try:
        created_todo = await todo_crud.create_todo(todo)
        
        # Convert TodoModel to TodoResponse format
        response_data = created_todo.to_response_dict()
        return TodoResponse(**response_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create todo: {str(e)}")


@router.put('/{todo_id}', response_model=TodoResponse)
async def update_todo(todo_id: str, todo_update: TodoUpdate):
    """
    Update an existing todo
    
    - **todo_id**: The ID of the todo to update (MongoDB ObjectId string)
    - **todo_update**: Updated todo data (all fields optional)
    """
    try:
        updated_todo = await todo_crud.update_todo(todo_id, todo_update)
        if not updated_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        # Convert TodoModel to TodoResponse format
        response_data = updated_todo.to_response_dict()
        return TodoResponse(**response_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update todo: {str(e)}")


@router.delete('/{todo_id}')
async def delete_todo(todo_id: str):
    """
    Delete a todo by ID
    
    - **todo_id**: The ID of the todo to delete (MongoDB ObjectId string)
    """
    try:
        deleted = await todo_crud.delete_todo(todo_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        return {"message": "Todo deleted successfully", "deleted_id": todo_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete todo: {str(e)}")


@router.get('/stats/count')
async def get_todos_count():
    """
    Get the total count of todos
    """
    try:
        count = await todo_crud.get_todos_count()
        return {"total_todos": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get todos count: {str(e)}")