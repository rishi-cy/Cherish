import requests
import os
import json
from datetime import datetime

BASE_URL = 'http://localhost:5000'

def test_database():
    """Test database connection and tables."""
    print("\nTesting database connection...")
    response = requests.get(f'{BASE_URL}/test/db')
    print(f"Database test response: {response.json()}")

def test_user_operations():
    """Test user registration and login."""
    print("\nTesting user operations...")
    
    # Test registration
    test_user = {
        'username': 'testuser',
        'password': 'Test123!'
    }
    response = requests.post(f'{BASE_URL}/register', data=test_user)
    print(f"Registration response: {response.text}")
    
    # Test login
    response = requests.post(f'{BASE_URL}/login', data=test_user)
    print(f"Login response: {response.text}")
    
    # Test user data retrieval
    response = requests.get(f'{BASE_URL}/test/user/{test_user["username"]}')
    print(f"User data response: {response.json()}")

def test_location_operations():
    """Test location operations."""
    print("\nTesting location operations...")
    
    # First login to get session
    login_data = {
        'username': 'testuser',
        'password': 'Test123!'
    }
    session = requests.Session()
    session.post(f'{BASE_URL}/login', data=login_data)
    
    # Test location upload
    location_data = {
        'name': 'Test Location',
        'description': 'Test Description',
        'experience': 'Test Experience',
        'latitude': 40.7128,
        'longitude': -74.0060
    }
    response = session.post(f'{BASE_URL}/upload_location', data=location_data)
    print(f"Location upload response: {response.text}")
    
    # Test location retrieval
    response = session.get(f'{BASE_URL}/test/location/1')
    print(f"Location data response: {response.json()}")

def test_file_upload():
    """Test file upload functionality."""
    print("\nTesting file upload...")
    
    # Create a test file
    test_file_path = 'test_image.jpg'
    with open(test_file_path, 'w') as f:
        f.write('Test image content')
    
    # Test file upload
    with open(test_file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(f'{BASE_URL}/test/upload', files=files)
        print(f"File upload response: {response.json()}")
    
    # Clean up test file
    os.remove(test_file_path)

def test_geocoding():
    """Test geocoding API functionality."""
    print("\nTesting geocoding API...")
    response = requests.get(f'{BASE_URL}/test/geocoding')
    print(f"Geocoding test response: {response.json()}")

def test_admin_functionality():
    """Test admin functionality."""
    print("\nTesting admin functionality...")
    
    # Login as admin
    admin_data = {
        'username': 'admin',
        'password': 'Admin123!'
    }
    session = requests.Session()
    response = session.post(f'{BASE_URL}/login', data=admin_data)
    print(f"Admin login response: {response.text}")
    
    # Test admin users view
    response = session.get(f'{BASE_URL}/admin/users')
    print(f"Admin users view response: {response.text}")

def main():
    """Run all tests."""
    print("Starting application tests...")
    
    try:
        test_database()
        test_user_operations()
        test_location_operations()
        test_file_upload()
        test_geocoding()
        test_admin_functionality()
        
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nError during testing: {str(e)}")

if __name__ == '__main__':
    main() 