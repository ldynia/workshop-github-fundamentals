import pytest

from run import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_api(client):
    response = client.get("/api/v1/movies/recommend")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()[0]["title"] != ""

    response = client.get("/api/v1/movies/recommend?title=Kingpin")
    assert response.status_code == 200
    assert response.is_json
    assert len(response.get_json()) >= 2

    response = client.get("/api/v1/movies/recommend?title=Lost%20in%20Translation")
    assert response.status_code == 200
    assert response.is_json
    assert len(response.get_json()) >= 5
