import pytest
import requests

@pytest.fixture
def api_url():
    return "http://127.0.0.1:8000"

def test_create_film(api_url):
    payload = {
        "title": "Inception",
        "year": 2010,
        "date_last_watched": "2024-04-15"
    }
    response = requests.post(f"{api_url}/film/", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Successfully added Film."

def test_get_films(api_url):
    # Test retrieving all films
    response = requests.get(f"{api_url}/films/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_film(api_url):
    response = requests.get(f"{api_url}/film/13")
    assert response.status_code == 200
    assert response.json().get("id") == 13

def test_update_film(api_url):
    payload = {
        "id": 1,  
        "date_last_watched": "2024-04-16"
    }
    response = requests.put(f"{api_url}/film/1", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Film updated successfully."

def test_delete_film(api_url):
    # Test deleting a film
    response = requests.delete(f"{api_url}/film/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Film deleted successfully."
