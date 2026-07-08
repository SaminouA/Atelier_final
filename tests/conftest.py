import pytest

from src.app import app, tasks


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    tasks.clear()

    with app.test_client() as client:
        yield client
