from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is working ..."}


def test_prediction():
    response = client.get("/predict/")
    assert response.status_code == 422
