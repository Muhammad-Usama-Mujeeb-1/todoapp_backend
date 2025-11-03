# User CRUD operations for database interactions
from typing import Optional
from datetime import datetime
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from app.core.database import get_collection
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import UserModel
from app.core.security import get_hash_password, verify_password

class UserCRUD:
    def __init__(self):
        self.collection_name = "users"
    
    async def create_user(self, user: UserCreate) -> UserModel:
        """Create a new user in database"""
        try:
            collection = get_collection(self.collection_name)
            
            # Check if user already exists
            existing_user = collection.find_one({
                "$or": [
                    {"email": user.email},
                    {"username": user.username}
                ]
            })
            
            if existing_user:
                if existing_user["email"] == user.email:
                    raise ValueError("User with this email already exists")
                if existing_user["username"] == user.username:
                    raise ValueError("User with this username already exists")
            
            # Create new user with hashed password
            hashed_password = get_hash_password(user.password)
            new_user = UserModel(
                email=user.email,
                username=user.username,
                hashed_password=hashed_password,
                full_name=user.full_name
            )
            
            # Insert into MongoDB
            result = collection.insert_one(new_user.to_dict())
            
            # Get the inserted document
            created_doc = collection.find_one({"_id": result.inserted_id})
            return UserModel.from_dict(created_doc)
            
        except Exception as e:
            print(f"Error creating user: {e}")
            raise
    
    async def get_user_by_email(self, email: str) -> Optional[UserModel]:
        """Get user by email"""
        try:
            collection = get_collection(self.collection_name)
            doc = collection.find_one({"email": email})
            
            if doc:
                return UserModel.from_dict(doc)
            return None
            
        except Exception as e:
            print(f"Error getting user by email: {e}")
            return None
    
    async def get_user_by_username(self, username: str) -> Optional[UserModel]:
        """Get user by username"""
        try:
            collection = get_collection(self.collection_name)
            doc = collection.find_one({"username": username})
            
            if doc:
                return UserModel.from_dict(doc)
            return None
            
        except Exception as e:
            print(f"Error getting user by username: {e}")
            return None
    
    async def get_user_by_id(self, user_id: str) -> Optional[UserModel]:
        """Get user by ID"""
        try:
            collection = get_collection(self.collection_name)
            
            # Convert string ID to ObjectId
            object_id = ObjectId(user_id)
            doc = collection.find_one({"_id": object_id})
            
            if doc:
                return UserModel.from_dict(doc)
            return None
            
        except Exception as e:
            print(f"Error getting user by ID: {e}")
            return None
    
    async def authenticate_user(self, email_or_username: str, password: str) -> Optional[UserModel]:
        """Authenticate user with email/username and password"""
        try:
            # Try to find user by email or username
            user = await self.get_user_by_email(email_or_username)
            if not user:
                user = await self.get_user_by_username(email_or_username)
            
            if not user:
                return None
            
            # Verify password
            if not verify_password(password, user.hashed_password):
                return None
            
            # # Check if user is active
            # if not user.is_active:
            #     return None
            
            return user
            
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None
    
    async def update_user(self, user_id: str, user_update: UserUpdate) -> Optional[UserModel]:
        """Update user information"""
        try:
            collection = get_collection(self.collection_name)
            
            # Convert string ID to ObjectId
            object_id = ObjectId(user_id)
            
            # Build update data
            update_data = {"updated_at": datetime.utcnow()}
            
            if user_update.email is not None:
                # Check if email is already taken by another user
                existing_user = collection.find_one({
                    "email": user_update.email,
                    "_id": {"$ne": object_id}
                })
                if existing_user:
                    raise ValueError("Email already taken by another user")
                update_data["email"] = user_update.email
                
            if user_update.username is not None:
                # Check if username is already taken by another user
                existing_user = collection.find_one({
                    "username": user_update.username,
                    "_id": {"$ne": object_id}
                })
                if existing_user:
                    raise ValueError("Username already taken by another user")
                update_data["username"] = user_update.username
                
            if user_update.full_name is not None:
                update_data["full_name"] = user_update.full_name
            
            # Update the document
            result = collection.update_one(
                {"_id": object_id},
                {"$set": update_data}
            )
            
            if result.matched_count > 0:
                # Return updated document
                updated_doc = collection.find_one({"_id": object_id})
                return UserModel.from_dict(updated_doc)
            
            return None
            
        except Exception as e:
            print(f"Error updating user: {e}")
            return None

# Create instance for use in API endpoints
user_crud = UserCRUD()