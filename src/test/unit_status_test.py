import pytest
import src.services.status_service as status
from fastapi.testclient import TestClient
from src.app import app
from src.test.conftest import mock_find_one, mock_insert_one

client = TestClient(app=app)


@pytest.mark.parametrize("endpoint,status_code,expected", [("/api", 200, True)])
def test_endpoint_available(endpoint: str, status_code: int, expected: bool):
    res = client.get(endpoint)

    contents = res.json()
    assert res.status_code == status_code
    assert contents["system"] == expected


@pytest.mark.asyncio
async def test_status_service(monkeypatch):
    srv = status.StatusService()
    monkeypatch.setattr(status, "insert_one", mock_insert_one)
    monkeypatch.setattr(status, "find_one", mock_find_one)
    result = await srv.health_check()

    assert result["some_property"] == 10
