# Main FastAPI application - organized structure
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.v1.api import api_router
from app.core.database import connect_to_mongo, close_connection
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager - handles startup/shutdown events"""
    # Startup
    print("🚀 Starting TodoApp API...")
    try:
        # Connect to MongoDB
        connect_to_mongo()
        print("✅ Database connected successfully")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    
    yield  # Application runs here
    
    # Shutdown
    print("🛑 Shutting down TodoApp API...")
    close_connection()
    print("📴 Database connection closed")

# Create FastAPI app instance
app = FastAPI(
    title="TodoApp API",
    description="A TodoApp backend built with FastAPI, MongoDB, and JWT authentication",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,  # Use configured origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
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
        "environment": settings.environment,
        "docs": "/docs",
        "endpoints": {
            "authentication": "/api/v1/auth",
            "todos": "/api/v1/todos",
            "health": "/health"
        }
    }

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment
    }