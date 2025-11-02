# User schemas for authentication
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base schema for User with common fields"""
    email: EmailStr = Field(
        ..., 
        description="User's email address",
        example="user@example.com"
    )
    username: str = Field(
        ..., 
        min_length=3, 
        max_length=50,
        description="Username (unique)",
        example="johndoe"
    )
    full_name: Optional[str] = Field(
        None, 
        description="User's full name",
        example="John Doe"
    )


class UserCreate(UserBase):
    """Schema for creating a new user (registration)"""
    password: str = Field(
        ..., 
        min_length=8,
        description="User password (will be hashed)",
        example="securepassword123"
    )


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    email: Optional[EmailStr] = Field(None, description="New email address")
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, description="New full name")


class UserResponse(UserBase):
    """Schema for user response (NO password)"""
    id: str = Field(
        ..., 
        description="User's unique identifier",
        example="507f1f77bcf86cd799439011"
    )
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """Schema for user login"""
    email_or_username: str = Field(
        ..., 
        description="Email or username",
        example="user@example.com"
    )
    password: str = Field(
        ..., 
        description="User password",
        example="securepassword123"
    )


class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str = Field(
        ..., 
        description="JWT access token"
    )
    token_type: str = Field(
        "bearer", 
        description="Token type"
    )
    expires_in: int = Field(
        ..., 
        description="Token expiration time in seconds",
        example=3600
    )