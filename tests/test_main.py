from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "online"}


def test_clear_db():
    response = client.delete("/clear_db")
    assert response.status_code == 200


def test_add_owners():
    response = client.post("/owners/5")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 5


def test_add_pets():
    response = client.post("/pets/50")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 50


def test_get_all_owners():
    response = client.get("/all/owners")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 5


def test_get_all_pets():
    response = client.get("/all/pets")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 50


def test_get_owner_by_id():
    response_ok = client.get("/owners/1")
    data = response_ok.json()
    response_bad = client.get("/owners/10")
    assert response_bad.status_code == 404
    assert response_ok.status_code == 200
    assert data["id"] == 1


def test_get_pet_by_id():
    response_ok = client.get("/pets/42")
    data = response_ok.json()
    response_bad = client.get("/pets/52")
    assert response_bad.status_code == 404
    assert response_ok.status_code == 200
    assert data["id"] == 42
