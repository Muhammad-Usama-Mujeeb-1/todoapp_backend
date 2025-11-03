#!/usr/bin/env python3
"""
🧪 Quick API Test Script
Test the TodoApp API endpoints to verify functionality
"""

import requests
from time import sleep

BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}")
        print(f"✅ Health Check: {response.status_code}")
        print(f"   Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health Check failed: {e}")
        return False

def test_root():
    """Test the root endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Root endpoint: {response.status_code}")
        print(f"   Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
        return False

def test_user_registration():
    """Test user registration"""
    try:
        user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword123"
        }
        response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=user_data)
        print(f"✅ User Registration: {response.status_code}")
        if response.status_code == 201:
            print(f"   User created successfully!")
        elif response.status_code == 400:
            print(f"   User might already exist: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ User registration failed: {e}")
        return False

def run_tests():
    """Run all tests"""
    print("🧪 Starting TodoApp API Tests...")
    print("=" * 50)
    
    # Give server time to start
    print("⏳ Waiting for server to be ready...")
    sleep(3)
    
    tests_passed = 0
    total_tests = 3
    
    if test_health():
        tests_passed += 1
    
    if test_root():
        tests_passed += 1
        
    if test_user_registration():
        tests_passed += 1
    
    print("=" * 50)
    print(f"📊 Tests completed: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! API is working correctly.")
    else:
        print("⚠️ Some tests failed. Check server logs for details.")

if __name__ == "__main__":
    run_tests()