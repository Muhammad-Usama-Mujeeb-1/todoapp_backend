# OAuth2 scheme for JWT token authentication
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import UserResponse
from app.crud.user import user_crud
from app.core.security import decode_access_token
from app.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.api_v1_str}/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserResponse:
    """Get current user from JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        # headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode JWT token
        user_id = decode_access_token(token)
        if user_id is None:
            raise credentials_exception
            
        # Get user from database
        user = await user_crud.get_user_by_id(user_id)
        if user is None:
            raise credentials_exception
            
        # # Check if user is active
        # if not user.is_active:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Inactive user account"
        #     )
            
        # Convert to response format
        response_data = user.to_response_dict()
        return UserResponse(**response_data)
        
    except Exception as e:
        raise credentials_exception