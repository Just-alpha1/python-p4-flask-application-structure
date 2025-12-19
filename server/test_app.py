
#!/usr/bin/env python3
import pytest
from app import app

def test_index_route():
    """Test the index route returns correct HTML"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'<h1>Python Operations with Flask Routing and Views</h1>' in response.data

def test_print_string_route():
    """Test the print_string route returns the parameter"""
    with app.test_client() as client:
        response = client.get('/print/hello')
        assert response.status_code == 200
        assert response.data == b'hello'

def test_count_route():
    """Test the count route returns numbers on separate lines"""
    with app.test_client() as client:
        response = client.get('/count/3')
        assert response.status_code == 200
        expected = b'1\n2\n3'
        assert response.data == expected

def test_count_route_single_number():
    """Test the count route with single number"""
    with app.test_client() as client:
        response = client.get('/count/1')
        assert response.status_code == 200
        assert response.data == b'1'

def test_math_addition():
    """Test the math route with addition"""
    with app.test_client() as client:
        response = client.get('/math/5/+/3')
        assert response.status_code == 200
        assert response.data == b'8'

def test_math_subtraction():
    """Test the math route with subtraction"""
    with app.test_client() as client:
        response = client.get('/math/10/-/4')
        assert response.status_code == 200
        assert response.data == b'6'

def test_math_multiplication():
    """Test the math route with multiplication"""
    with app.test_client() as client:
        response = client.get('/math/3/*/4')
        assert response.status_code == 200
        assert response.data == b'12'

def test_math_division():
    """Test the math route with division"""
    with app.test_client() as client:
        response = client.get('/math/10/div/2')
        assert response.status_code == 200
        assert response.data == b'5'

def test_math_modulo():
    """Test the math route with modulo"""
    with app.test_client() as client:
        response = client.get('/math/10/%/3')
        assert response.status_code == 200
        assert response.data == b'1'

def test_math_invalid_operation():
    """Test the math route with invalid operation"""
    with app.test_client() as client:
        response = client.get('/math/5/^/3')
        assert response.status_code == 400

def test_flask_app_exists():
    """Test that Flask app instance exists"""
    assert app is not None
    assert app.name == 'app'

if __name__ == '__main__':
    pytest.main([__file__])
