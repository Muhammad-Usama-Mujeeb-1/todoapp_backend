# Todo CRUD operations for database interactions
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from app.core.database import get_collection
from app.schemas.todo import TodoCreate, TodoUpdate, PriorityLevel, TodoStatus
from app.models.todo import TodoModel

class TodoCRUD:
    def __init__(self):
        self.collection_name = "todos"
    
    async def create_todo(self, todo: TodoCreate, user_id: str = "default_user") -> TodoModel:
        """Create a new todo in database"""
        try:
            collection = get_collection(self.collection_name)
            
            # Create TodoModel instance
            new_todo = TodoModel(
                todo_name=todo.todo_name,
                todo_description=todo.todo_description,
                priority=todo.priority,
                status=todo.status,
                user_id=user_id
            )
            
            # Insert into MongoDB
            result = collection.insert_one(new_todo.to_dict())
            
            # Get the inserted document
            created_doc = collection.find_one({"_id": result.inserted_id})
            return TodoModel.from_dict(created_doc)
            
        except Exception as e:
            print(f"Error creating todo: {e}")
            raise
    
    async def get_todo(self, todo_id: str, user_id: str = "default_user") -> Optional[TodoModel]:
        """Get a todo by ID"""
        try:
            collection = get_collection(self.collection_name)
            
            # Convert string ID to ObjectId
            object_id = ObjectId(todo_id)
            
            # Find the document
            doc = collection.find_one({
                "_id": object_id, 
                "user_id": user_id
            })
            
            if doc:
                return TodoModel.from_dict(doc)
            return None
            
        except Exception as e:
            print(f"Error getting todo {todo_id}: {e}")
            return None
    
    async def get_todos(
        self, 
        user_id: str = "default_user", 
        skip: int = 0, 
        limit: int = 100,
        status_filter: Optional[TodoStatus] = None,
        priority_filter: Optional[PriorityLevel] = None
    ) -> List[TodoModel]:
        """Get all todos for a user with optional filtering"""
        try:
            collection = get_collection(self.collection_name)
            
            # Build query filter
            query = {"user_id": user_id}
            
            if status_filter:
                query["status"] = status_filter.value
                
            if priority_filter:
                query["priority"] = priority_filter.value
            
            # Find documents with pagination
            cursor = collection.find(query).skip(skip).limit(limit).sort("created_at", -1)
            
            todos = []
            for doc in cursor:
                todos.append(TodoModel.from_dict(doc))
            
            return todos
            
        except Exception as e:
            print(f"Error getting todos: {e}")
            return []
    
    async def update_todo(self, todo_id: str, todo_update: TodoUpdate, user_id: str = "default_user") -> Optional[TodoModel]:
        """Update a todo"""
        try:
            collection = get_collection(self.collection_name)
            
            # Convert string ID to ObjectId
            object_id = ObjectId(todo_id)
            
            # Build update data - only include fields that are not None
            update_data = {"updated_at": datetime.utcnow()}
            
            if todo_update.todo_name is not None:
                update_data["todo_name"] = todo_update.todo_name
            if todo_update.todo_description is not None:
                update_data["todo_description"] = todo_update.todo_description
            if todo_update.priority is not None:
                update_data["priority"] = todo_update.priority.value
            if todo_update.status is not None:
                update_data["status"] = todo_update.status.value
            
            # Update the document
            result = collection.update_one(
                {"_id": object_id, "user_id": user_id},
                {"$set": update_data}
            )
            
            if result.matched_count > 0:
                # Return updated document
                updated_doc = collection.find_one({"_id": object_id})
                return TodoModel.from_dict(updated_doc)
            
            return None
            
        except Exception as e:
            print(f"Error updating todo {todo_id}: {e}")
            return None
    
    async def delete_todo(self, todo_id: str, user_id: str = "default_user") -> bool:
        """Delete a todo"""
        try:
            collection = get_collection(self.collection_name)
            
            # Convert string ID to ObjectId
            object_id = ObjectId(todo_id)
            
            # Delete the document
            result = collection.delete_one({
                "_id": object_id, 
                "user_id": user_id
            })
            
            return result.deleted_count > 0
            
        except Exception as e:
            print(f"Error deleting todo {todo_id}: {e}")
            return False
    
    async def get_todos_count(self, user_id: str = "default_user") -> int:
        """Get total count of todos for a user"""
        try:
            collection = get_collection(self.collection_name)
            return collection.count_documents({"user_id": user_id})
        except Exception as e:
            print(f"Error counting todos: {e}")
            return 0
    
    async def get_todos_by_status(self, status: TodoStatus, user_id: str = "default_user") -> List[TodoModel]:
        """Get all todos with specific status"""
        return await self.get_todos(user_id=user_id, status_filter=status)

# Create instance for use in API endpoints
todo_crud = TodoCRUD()