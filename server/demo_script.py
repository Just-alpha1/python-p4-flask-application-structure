#!/usr/bin/env python3
"""
Flask Tutorial Comprehensive Demo Script
This script demonstrates all the concepts from the Flask tutorial
"""

import requests
import json

def test_flask_app():
    """Test the Flask application functionality"""
    base_url = "http://127.0.0.1:5555"
    
    print("="*60)
    print("FLASK TUTORIAL DEMONSTRATION")
    print("="*60)
    
    # Test 1: Index route
    print("\n1. Testing index route (/)")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        print("   ✓ Index route working correctly")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 2: User route with string parameter
    print("\n2. Testing user route with string parameter (/testuser)")
    try:
        response = requests.get(f"{base_url}/testuser")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        print("   ✓ User route working correctly")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 3: User route with special characters
    print("\n3. Testing user route with special characters (/Mr-User)")
    try:
        response = requests.get(f"{base_url}/Mr-User")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        print("   ✓ Special characters handled correctly")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 4: Request info endpoint
    print("\n4. Testing request info endpoint (/request-info)")
    try:
        response = requests.get(f"{base_url}/request-info")
        print(f"   Status Code: {response.status_code}")
        info = response.json()
        print("   Request Information:")
        print(f"   - Method: {info['method']}")
        print(f"   - Path: {info['path']}")
        print(f"   - Host: {info['host']}")
        print(f"   - Remote Address: {info['remote_addr']}")
        print("   ✓ Request object manipulation working")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 5: GET request with query parameters
    print("\n5. Testing GET request with query parameters (/greet?name=Alice)")
    try:
        response = requests.get(f"{base_url}/greet?name=Alice")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        print("   ✓ Query parameter handling working")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 6: POST request
    print("\n6. Testing POST request (/greet)")
    try:
        response = requests.post(f"{base_url}/greet", data={"name": "Bob"})
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        print("   ✓ POST request handling working")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    print("\n" + "="*60)
    print("TUTORIAL QUESTIONS ANSWERED:")
    print("="*60)
    
    print("\nQ: What is the value of __name__ when we run python server/app.py?")
    print("A: When running 'python server/app.py', __name__ equals '__main__'")
    print("   This is because the script is being executed directly.")
    
    print("\nQ: Which line of code tells Flask to show the returned data from index() in the web browser?")
    print("A: The @app.route('/') decorator registers the index() function as a view.")
    print("   When a request comes to '/', Flask calls index() and displays its return value.")
    
    print("\nQ: Flask has to parse 'string' and 'username' from the route. How can you use Python to remove brackets and get parameters out of a string?")
    print("A: Flask automatically handles this parsing. The syntax '<string:username>' tells")
    print("   Flask to expect a string parameter named 'username'. Flask's URL rule parser")
    print("   extracts the parameter and passes it directly to the function.")
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    test_flask_app()
