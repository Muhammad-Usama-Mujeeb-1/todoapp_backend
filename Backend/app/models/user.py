# User database model (MongoDB document structure)
# TODO: Add your User MongoDB document models here
# Example structure:

# from datetime import datetime
# from typing import Optional
# from bson import ObjectId
#
# class UserModel:
#     """MongoDB document model for User"""
#     
#     def __init__(
#         self,
#         email: str,
#         username: str,
#         hashed_password: str,
#         full_name: Optional[str] = None,
#         _id: Optional[ObjectId] = None,
#         created_at: Optional[datetime] = None,
#         is_active: bool = True
#     ):
#         self._id = _id or ObjectId()
#         self.email = email
#         self.username = username
#         self.hashed_password = hashed_password
#         self.full_name = full_name
#         self.created_at = created_at or datetime.utcnow()
#         self.is_active = is_active
#
#     def to_dict(self):
#         """Convert to dictionary for MongoDB storage"""
#         return {
#             "_id": self._id,
#             "email": self.email,
#             "username": self.username,
#             "hashed_password": self.hashed_password,
#             "full_name": self.full_name,
#             "created_at": self.created_at,
#             "is_active": self.is_active
#         }