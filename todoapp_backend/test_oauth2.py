#!/usr/bin/env python3
"""
🔧 Test OAuth2 Form Login
Test the OAuth2PasswordRequestForm endpoint for Swagger UI compatibility
"""

import requests
from urllib.parse import urlencode

BASE_URL = "http://localhost:8000"

def test_oauth2_form_login():
    """Test OAuth2 form-based login (what Swagger UI uses)"""
    print("🔧 Testing OAuth2 form-based login...")
    
    # OAuth2 form data (what Swagger UI sends)
    form_data = {
        "username": "test@example.com",  # This can be email or username
        "password": "testpassword123"
    }
    
    try:
        print(f"📤 Sending OAuth2 form request: {form_data}")
        response = requests.post(
            f"{BASE_URL}/api/v1/auth/token",  # Use /token endpoint
            data=form_data,  # Use data= for form encoding, not json=
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        print(f"📥 Response Status: {response.status_code}")
        print(f"📄 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ OAuth2 Login successful:")
            token_data = response.json()
            print(f"   Access Token: {token_data['access_token'][:50]}...")
            print(f"   Token Type: {token_data['token_type']}")
            return True
        else:
            print(f"❌ Login failed with status: {response.status_code}")
            try:
                error_detail = response.json()
                print(f"   Error: {error_detail}")
            except:
                print(f"   Raw response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

def test_json_login():
    """Test JSON-based login endpoint"""
    print("📄 Testing JSON-based login...")
    
    login_data = {
        "email_or_username": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/auth/login",  # Use /login endpoint
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"📥 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ JSON Login successful:")
            token_data = response.json()
            print(f"   Access Token: {token_data['access_token'][:50]}...")
            return True
        else:
            print(f"❌ JSON Login failed: {response.status_code}")
            try:
                error_detail = response.json()
                print(f"   Error: {error_detail}")
            except:
                print(f"   Raw response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ JSON Request failed: {e}")
        return False

def main():
    print("🧪 Testing OAuth2 Authentication for Swagger UI")
    print("=" * 60)
    
    # Test both endpoints
    oauth2_works = test_oauth2_form_login()
    print()
    json_works = test_json_login()
    
    print("\n" + "=" * 60)
    print("📊 Test Results:")
    print(f"   OAuth2 Form Login (Swagger UI): {'✅ WORKS' if oauth2_works else '❌ FAILED'}")
    print(f"   JSON Login (API clients): {'✅ WORKS' if json_works else '❌ FAILED'}")
    
    if oauth2_works:
        print("\n🎉 Swagger UI authentication should now work!")
        print("   Go to http://localhost:8000/docs")
        print("   Click 'Authorize' button")
        print("   Enter your credentials (username: test@example.com, password: testpassword123)")
    else:
        print("\n⚠️ OAuth2 authentication needs fixing for Swagger UI")

if __name__ == "__main__":
    main()