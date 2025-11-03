# Authentication endpoints (JWT login, register, etc.)
from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.auth import get_current_user
from app.schemas.user import UserCreate, UserResponse, UserLogin, Token
from app.crud.user import user_crud
from app.core.security import create_access_token
from app.core.config import settings


router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    """
    Register a new user
    
    - **email**: Valid email address (must be unique)
    - **username**: Username 3-50 characters (must be unique)
    - **password**: Password minimum 8 characters
    - **full_name**: Optional full name
    """
    try:
        # Create new user
        created_user = await user_crud.create_user(user)
        
        # Convert to response format
        response_data = created_user.to_response_dict()
        return UserResponse(**response_data)
        
    except ValueError as e:
        # Handle duplicate email/username
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create user: {str(e)}"
        )


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token endpoint for Swagger UI
    
    - **username**: Email address or username
    - **password**: User password
    
    Returns JWT token for authenticated requests
    """
    try:
        print(f"🔑 OAuth2 login attempt - username: {form_data.username}")
        
        # Authenticate user using the username field (which can be email or username)
        user = await user_crud.authenticate_user(
            form_data.username, 
            form_data.password
        )
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email/username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Create access token
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token = create_access_token(str(user._id), expires_delta=access_token_expires)
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": settings.access_token_expire_minutes * 60  # Convert to seconds
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ OAuth2 Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Login failed: {str(e)}"
        )


@router.post("/login", response_model=Token)
async def login_with_json(user_credentials: UserLogin):
    """
    JSON-based login endpoint for API clients
    
    - **email_or_username**: Email address or username
    - **password**: User password
    
    Returns JWT token for authenticated requests
    """
    try:
        print(f"🔑 JSON login attempt - user: {user_credentials.email_or_username}")
        
        # Authenticate user
        user = await user_crud.authenticate_user(
            user_credentials.email_or_username, 
            user_credentials.password
        )
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email/username or password",
            )
        
        # Create access token
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token = create_access_token(str(user._id), expires_delta=access_token_expires)
        
        return Token(
            access_token=access_token,
            token_type="bearer",
            expires_in=settings.access_token_expire_minutes * 60  # Convert to seconds
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ JSON Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Login failed: {str(e)}"
        )






@router.get("/get_current_user", response_model=UserResponse)
async def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    """
    Get current authenticated user information
    
    Requires valid JWT token in Authorization header:
    Authorization: Bearer <your-jwt-token>
    """
    return current_user


@router.get("/verify-token")
async def verify_token(current_user: UserResponse = Depends(get_current_user)):
    """
    Verify if JWT token is valid and not expired
    
    Returns user information if token is valid
    """
    return {
        "valid": True,
        "user_id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }