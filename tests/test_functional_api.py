from fastapi.testclient import TestClient
from discolog.api import api

client = TestClient(api)


def test_create_album_via_api():
    response = client.post(
        "/albums/",
        json={
            "name": "Summer Holiday",
            "artist": "Dreamcatcher",
            "year": 2021,
            "rate": 10,
            "review": "Fez tanto por mim, não sei nem o que dizer.",
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "Summer Holiday"
    assert result["id"] == 1
