# Security utilities (JWT, password hashing, etc.)
# TODO: Add your JWT and security logic here
# Example structure:

# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from app.core.config import settings
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)
#
# def get_password_hash(password):
#     return pwd_context.hash(password)
#
# def create_access_token(data: dict, expires_delta: timedelta = None):
#     # JWT token creation logic