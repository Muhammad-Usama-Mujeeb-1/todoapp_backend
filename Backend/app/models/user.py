# User database model (MongoDB document structure)
from datetime import datetime
from typing import Optional
from bson import ObjectId

class UserModel:
    """MongoDB document model for User"""
    
    def __init__(
        self,
        email: str,
        username: str,
        hashed_password: str,
        full_name: Optional[str] = None,
        _id: Optional[ObjectId] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self._id = _id or ObjectId()
        self.email = email
        self.username = username
        self.hashed_password = hashed_password
        self.full_name = full_name
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self):
        """Convert to dictionary for MongoDB storage"""
        return {
            "_id": self._id,
            "email": self.email,
            "username": self.username,
            "hashed_password": self.hashed_password,
            "full_name": self.full_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, doc: dict):
        """Create UserModel instance from MongoDB document"""
        return cls(
            _id=doc.get("_id"),
            email=doc["email"],
            username=doc["username"],
            hashed_password=doc["hashed_password"],
            full_name=doc.get("full_name"),
            created_at=doc.get("created_at"),
            updated_at=doc.get("updated_at"),
        )

    def to_response_dict(self):
        """Convert to dictionary for API responses (no password)"""
        return {
            "id": str(self._id),
            "email": self.email,
            "username": self.username,
            "full_name": self.full_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }