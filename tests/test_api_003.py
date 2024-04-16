import pytest
from sqlalchemy import create_engine
from filmdiary import Base
from filmdiary.api.api import create_app
from fastapi.testclient import TestClient
import os

@pytest.fixture
def test_client():
    engine = create_engine('sqlite:///test_film_database.db')
    app = create_app(engine)
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="session", autouse=True)
def cleanup_test_database(request):
    engine = create_engine('sqlite:///test_film_database.db')
    Base.metadata.drop_all(engine)

    def finalize():
        os.remove("test_film_database.db")

    request.addfinalizer(finalize)

def test_create_film(test_client):
    payload = {
        "title": "Inception",
        "year": 2010,
        "date_last_watched": "2024-04-15"
    }
    response = test_client.post("/film/", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Successfully added Film."

def test_get_films(test_client):
    response = test_client.get("/films/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_film(test_client):
    response = test_client.get("/film/1")
    assert response.status_code == 200
    assert response.json().get("id") == 1

def test_update_film(test_client):
    payload = {
        "id": 1,  
        "date_last_watched": "2024-04-16"
    }
    response = test_client.put("/film/1", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Film updated successfully."

def test_delete_film(test_client):
    response = test_client.delete("/film/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Film deleted successfully."