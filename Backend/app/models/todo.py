# Todo database model (MongoDB document structure)
# TODO: Add your MongoDB document models here
# Example structure for when you integrate with MongoDB:

# from datetime import datetime
# from typing import Optional
# from bson import ObjectId
# from app.schemas.todo import PriorityLevel
#
# class TodoModel:
#     """MongoDB document model for Todo"""
#     
#     def __init__(
#         self,
#         todo_name: str,
#         todo_description: str,
#         priority: PriorityLevel,
#         user_id: str,
#         _id: Optional[ObjectId] = None,
#         created_at: Optional[datetime] = None,
#         updated_at: Optional[datetime] = None,
#         completed: bool = False
#     ):
#         self._id = _id or ObjectId()
#         self.todo_name = todo_name
#         self.todo_description = todo_description
#         self.priority = priority
#         self.user_id = user_id
#         self.created_at = created_at or datetime.utcnow()
#         self.updated_at = updated_at or datetime.utcnow()
#         self.completed = completed
#
#     def to_dict(self):
#         """Convert to dictionary for MongoDB storage"""
#         return {
#             "_id": self._id,
#             "todo_name": self.todo_name,
#             "todo_description": self.todo_description,
#             "priority": self.priority,
#             "user_id": self.user_id,
#             "created_at": self.created_at,
#             "updated_at": self.updated_at,
#             "completed": self.completed
#         }