# Application configuration settings
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 🎯 Application Info
    app_name: str = "TodoApp FastAPI Backend"
    app_version: str = "1.0.0"
    environment: str = "development"
    debug: bool = True
    
    # 🗄️ Database Configuration
    mongodb_url: str
    database_name: str
    
    # 🔒 Security Configuration
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # 🌐 API Configuration
    api_v1_str: str = "/api/v1"
    backend_cors_origins: List[str] = ["http://localhost:3000", "http://localhost:8000", "http://localhost:8080"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# 🎯 Global settings instance
settings = Settings()