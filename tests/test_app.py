import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Get an activity name
    activities = client.get("/activities").json()
    activity_name = next(iter(activities.keys()))
    email = "testuser@mergington.edu"

    # Sign up
    signup_resp = client.post("/signup", json={"activity": activity_name, "email": email})
    assert signup_resp.status_code == 200
    assert "signed up" in signup_resp.json()["message"].lower()

    # Try duplicate signup
    dup_resp = client.post("/signup", json={"activity": activity_name, "email": email})
    assert dup_resp.status_code == 400 or "already" in dup_resp.json().get("message", "").lower()

    # Unregister
    unregister_resp = client.post("/unregister", json={"activity": activity_name, "email": email})
    assert unregister_resp.status_code == 200
    assert "removed" in unregister_resp.json()["message"].lower() or unregister_resp.json()["message"]

    # Unregister again (should fail or say not found)
    unregister_again = client.post("/unregister", json={"activity": activity_name, "email": email})
    assert unregister_again.status_code == 400 or "not found" in unregister_again.json().get("message", "").lower()