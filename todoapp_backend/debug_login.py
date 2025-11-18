#!/usr/bin/env python3
"""
🔍 Debug Login Issues
Test the login endpoint to see what validation errors are occurring
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_login_detailed():
    """Test login with detailed error reporting"""
    print("🔍 Testing login endpoint for validation errors...")
    
    # Test data that should work
    login_data = {
        "email_or_username": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        print(f"📤 Sending login request: {login_data}")
        response = requests.post(
            f"{BASE_URL}/api/v1/auth/login", 
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"📥 Response Status: {response.status_code}")
        print(f"📄 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 422:
            print("❌ Validation Error (422):")
            try:
                error_detail = response.json()
                print(json.dumps(error_detail, indent=2))
            except:
                print("Could not parse error response as JSON")
                print(f"Raw response: {response.text}")
        elif response.status_code == 200:
            print("✅ Login successful:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Request failed: {e}")

def test_register_first():
    """Register a user first to ensure we have valid credentials"""
    print("👤 Testing user registration first...")
    
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=user_data)
        print(f"Registration Status: {response.status_code}")
        
        if response.status_code == 201:
            print("✅ User registered successfully")
            return True
        elif response.status_code == 400:
            error = response.json()
            if "already exists" in error.get("detail", ""):
                print("✅ User already exists (that's fine)")
                return True
            else:
                print(f"❌ Registration error: {error}")
                return False
        else:
            print(f"❌ Registration failed: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Registration request failed: {e}")
        return False

def main():
    print("🧪 Debugging Login Issues")
    print("=" * 50)
    
    # First register a user
    if test_register_first():
        print("\n" + "=" * 50)
        # Then test login
        test_login_detailed()
    
    print("\n" + "=" * 50)
    print("🏁 Debug complete")

if __name__ == "__main__":
    main()