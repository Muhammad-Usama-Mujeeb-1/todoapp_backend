# Main API router that combines all endpoints
from fastapi import APIRouter

from app.api.v1.endpoints import todos, auth

api_router = APIRouter()

# Include authentication routes (public endpoints)
api_router.include_router(
    auth.router, 
    prefix="/auth", 
    tags=["🔐 Authentication"]
)

# Include todo routes (protected endpoints)
api_router.include_router(
    todos.router, 
    prefix="/todos", 
    tags=["📝 Todos"]
)