from fastapi.testclient import TestClient
from ..main import app


class TestService(object):
    def __new__(cls):
        return TestClient(app=app)
