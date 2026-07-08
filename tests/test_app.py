def test_home_returns_app_info(client):
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["app"] == "Todo API"
    assert data["status"] == "ok"
    assert "version" in data


def test_health_returns_healthy(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_get_tasks_empty(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    response = client.post("/tasks", json={"title": "Test task"})

    assert response.status_code == 201
    data = response.get_json()
    assert data["id"] == 1
    assert data["title"] == "Test task"
    assert data["done"] is False


def test_create_task_missing_title(client):
    response = client.post("/tasks", json={})

    assert response.status_code == 400
