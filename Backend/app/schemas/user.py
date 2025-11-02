# User schemas for authentication
# TODO: Add your user-related Pydantic schemas here
# Example structure:

# from typing import Optional
# from pydantic import BaseModel, EmailStr, Field
#
# class UserBase(BaseModel):
#     email: EmailStr
#     username: str
#     full_name: Optional[str] = None
#     is_active: bool = True
#
# class UserCreate(UserBase):
#     password: str
#
# class UserResponse(UserBase):
#     id: str
#     
#     class Config:
#         from_attributes = True
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str