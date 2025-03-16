import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# Mock the execute_aider_command function
def mock_execute_aider_command(command, params):
    if command == "/read":
        return "Mocked aider output"
    else:
        raise ValueError("Mocked error")


# Monkeypatch the execute_aider_command function during tests
@pytest.fixture(autouse=True)
def mock_aider(monkeypatch):
    monkeypatch.setattr("app.main.execute_aider_command", mock_execute_aider_command)


def test_execute_valid_command():
    response = client.post("/execute/", json={"command": "/read", "params": ""})
    assert response.status_code == 200
    assert response.json() == {"command": "/read", "result": "Mocked aider output"}


def test_execute_invalid_command():
    response = client.post("/execute/", json={"command": "/invalid", "params": ""})
    assert response.status_code == 400
    assert "Command '/invalid' is not allowed." in response.text


def test_execute_missing_params():
    # Test case where params are missing, but not necessarily invalid for the command
    response = client.post("/execute/", json={"command": "/read"})
    assert response.status_code == 422  # Expecting Unprocessable Entity due to Pydantic validation
