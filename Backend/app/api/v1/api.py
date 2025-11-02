# Main API router that combines all endpoints
from fastapi import APIRouter

from app.api.v1.endpoints import todos, auth

api_router = APIRouter()

# Include todo routes
api_router.include_router(
    todos.router, 
    prefix="/todos", 
    tags=["todos"]
)

# Include authentication routes  
api_router.include_router(
    auth.router, 
    prefix="/auth", 
    tags=["authentication"]
)