# Todo database model (MongoDB document structure)
from datetime import datetime
from typing import Optional
from bson import ObjectId
from app.schemas.todo import PriorityLevel, TodoStatus

class TodoModel:
    """MongoDB document model for Todo"""
    
    def __init__(
        self,
        name: str,
        description: str,
        priority: PriorityLevel = PriorityLevel.LOW,
        status: TodoStatus = TodoStatus.NOT_STARTED,
        user_id: str = "default_user",  # For now, until auth is implemented
        _id: Optional[ObjectId] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self._id = _id or ObjectId()
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
        self.user_id = user_id
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self):
        """Convert to dictionary for MongoDB storage"""
        return {
            "_id": self._id,
            "name": self.name,
            "description": self.description,
            "priority": self.priority.value,
            "status": self.status.value,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, doc: dict):
        """Create TodoModel instance from MongoDB document"""
        return cls(
            _id=doc.get("_id"),
            name=doc["name"],
            description=doc["description"],
            priority=PriorityLevel(doc.get("priority", PriorityLevel.LOW.value)),
            status=TodoStatus(doc.get("status", TodoStatus.NOT_STARTED.value)),
            user_id=doc.get("user_id", "default_user"),
            created_at=doc.get("created_at"),
            updated_at=doc.get("updated_at")
        )

    def to_response_dict(self):
        """Convert to dictionary for API responses"""
        return {
            "id": str(self._id),
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }