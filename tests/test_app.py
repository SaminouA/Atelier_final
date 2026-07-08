def test_index_returns_app_info(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "app": "Todo API",
        "status": "ok",
        "version": "1.0.0",
    }


def test_health_returns_healthy(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_version_returns_current_version(client):
    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0.0"}


def test_get_tasks_returns_empty_list(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task_returns_created_task(client):
    response = client.post("/tasks", json={"title": "Apprendre Cloud Run"})

    assert response.status_code == 201
    assert response.get_json() == {
        "id": 1,
        "title": "Apprendre Cloud Run",
        "done": False,
    }


def test_get_tasks_returns_created_tasks(client):
    client.post("/tasks", json={"title": "Ecrire les tests"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 1,
            "title": "Ecrire les tests",
            "done": False,
        }
    ]


def test_create_task_without_title_returns_error(client):
    response = client.post("/tasks", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "title is required"}
