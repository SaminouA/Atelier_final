def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "app": "Todo API",
        "status": "ok",
        "version": "1.0.0",
    }
