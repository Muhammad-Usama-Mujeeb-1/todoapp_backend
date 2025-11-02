# Database configuration and connection
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from typing import Optional

# TODO: Move this to environment variables for production security
# For now, using your existing connection string
# In production, use: MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_URL = "mongodb+srv://usamamujeeb:usama4528@cluster0.lmtb6a8.mongodb.net/Learning?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "Learning"  # TODO: Move to environment variables

# Global MongoDB client
client: Optional[MongoClient] = None
database = None

def connect_to_mongo():
    """Initialize MongoDB connection"""
    global client, database
    try:
        client = MongoClient(MONGODB_URL)
        database = client[DATABASE_NAME]
        # Test the connection
        client.admin.command('ping')
        print("✅ Connected to MongoDB successfully!")
        return database
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        raise

def get_database():
    """Get database instance"""
    global database
    if database is None:
        database = connect_to_mongo()
    return database

def close_connection():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        print("📴 MongoDB connection closed")