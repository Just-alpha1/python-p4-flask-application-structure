#!/usr/bin/env python3

import sys
sys.path.insert(0, '.')

from app import app

def test_app():
    """Simple test to verify the Flask app routes work"""
    with app.test_client() as client:
        print("Testing index route...")
        response = client.get('/')
        print(f"Status: {response.status_code}")
        print(f"Data: {response.data.decode()}")
        assert response.status_code == 200
        assert b'Python Operations with Flask Routing and Views' in response.data
        
        print("\nTesting print route...")
        response = client.get('/print/hello')
        print(f"Status: {response.status_code}")
        print(f"Data: {response.data.decode()}")
        assert response.status_code == 200
        assert response.data == b'hello'
        
        print("\nTesting count route...")
        response = client.get('/count/3')
        print(f"Status: {response.status_code}")
        print(f"Data: {response.data.decode()}")
        assert response.status_code == 200
        expected = '1\n2\n3'
        assert response.data.decode() == expected
        
        print("\nTesting math route...")
        response = client.get('/math/5/+/3')
        print(f"Status: {response.status_code}")
        print(f"Data: {response.data.decode()}")
        assert response.status_code == 200
        assert response.data == b'8'
        
        print("\nAll tests passed!")

if __name__ == '__main__':
    test_app()
