# Test configuration and fixtures
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """Test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture
def sample_todo():
    """Sample todo data for testing"""
    return {
        "todo_name": "Test Todo",
        "todo_description": "This is a test todo",
        "priority": 1
    }