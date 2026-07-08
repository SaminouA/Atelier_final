def test_index_returns_message(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, world!"}


def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
