from fastapi.testclient import TestClient
from ...app import app

client = TestClient(app=app)


def test_service_available():
    res = client.get("/")
    assert res.status_code == 200
