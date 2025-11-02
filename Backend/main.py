# Main FastAPI application - organized structure
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router

# Create FastAPI app instance
app = FastAPI(
    title="TodoApp API",
    description="A TodoApp backend built with FastAPI, MongoDB, and JWT authentication",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Health check endpoint
@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Welcome to TodoApp API", 
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Your original API logic is now organized in:
# - Schemas: app/schemas/todo.py
# - API Routes: app/api/v1/endpoints/todos.py
# - Database Models: app/models/todo.py (for MongoDB integration)
# - CRUD Operations: app/crud/todo.py (for MongoDB operations)