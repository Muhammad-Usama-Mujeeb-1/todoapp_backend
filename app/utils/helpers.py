# Common utility functions
# TODO: Add your utility functions here
# Example structure:

# from datetime import datetime
# from typing import Any, Dict
# from bson import ObjectId
#
# def convert_objectid_to_str(obj: Dict[str, Any]) -> Dict[str, Any]:
#     """Convert MongoDB ObjectId to string for JSON serialization"""
#     if "_id" in obj and isinstance(obj["_id"], ObjectId):
#         obj["_id"] = str(obj["_id"])
#     return obj
#
# def get_current_timestamp() -> datetime:
#     """Get current UTC timestamp"""
#     return datetime.utcnow()
#
# def format_response(data: Any, message: str = "Success") -> Dict[str, Any]:
#     """Format API response"""
#     return {
#         "success": True,
#         "message": message,
#         "data": data
#     }