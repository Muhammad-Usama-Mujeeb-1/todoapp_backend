# Database configuration and connection
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import Optional
from app.core.config import settings

# Global MongoDB client
client: Optional[MongoClient] = None
database = None

def connect_to_mongo():
    """Initialize MongoDB connection using environment variables"""
    global client, database
    try:
        print(f"🔌 Connecting to MongoDB: {settings.database_name}")
        client = MongoClient(settings.mongodb_url)
        database = client[settings.database_name]
        # Test the connection
        client.admin.command('ping')
        print(f"✅ Connected to MongoDB successfully! Database: {settings.database_name}")
        return database
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        print(f"🔍 Check your .env file and MongoDB Atlas network access")
        raise

def get_database():
    """Get database instance"""
    global database
    if database is None:
        database = connect_to_mongo()
    return database

def get_collection(collection_name: str):
    """Get a specific collection from the database"""
    db = get_database()
    return db[collection_name]

def close_connection():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        print("📴 MongoDB connection closed")