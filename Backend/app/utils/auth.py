# Authentication dependencies and utilities
# TODO: Add your authentication dependencies here
# Example structure:

# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from app.core.security import SECRET_KEY, ALGORITHM
# from app.crud.user import user_crud
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     """Get current authenticated user"""
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: str = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     
#     user = await user_crud.get_user_by_id(user_id)
#     if user is None:
#         raise credentials_exception
#     return user