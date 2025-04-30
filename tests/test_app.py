from src.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_activities():
    """Test retrieving all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()

def test_signup_for_activity_success():
    """Test signing up a student successfully"""
    response = client.post("/activities/Chess Club/signup", params={"email": "newstudent@mergington.edu"})
    assert response.status_code == 200
    assert response.json() == {"message": "Signed up newstudent@mergington.edu for Chess Club"}

def test_signup_for_activity_already_signed_up():
    """Test signing up a student who is already signed up"""
    response = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}

def test_signup_for_nonexistent_activity():
    """Test signing up for a nonexistent activity"""
    response = client.post("/activities/Nonexistent Activity/signup", params={"email": "student@mergington.edu"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}

def test_cancel_signup_success():
    """Test canceling a student's signup successfully"""
    response = client.delete("/activities/Chess Club/cancel", params={"email": "michael@mergington.edu"})
    assert response.status_code == 200
    assert response.json() == {"message": "Canceled signup for michael@mergington.edu from Chess Club"}

def test_cancel_signup_not_signed_up():
    """Test canceling a signup for a student not signed up"""
    response = client.delete("/activities/Chess Club/cancel", params={"email": "not_signed_up@mergington.edu"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is not signed up for this activity"}

def test_cancel_signup_nonexistent_activity():
    """Test canceling a signup for a nonexistent activity"""
    response = client.delete("/activities/Nonexistent Activity/cancel", params={"email": "student@mergington.edu"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}