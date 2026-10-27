from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_create_and_get_task():
    response = client.post("/tasks", json={"title": "Study FastAPI"})
    assert response.status_code == 201
    task_id = response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Study FastAPI"