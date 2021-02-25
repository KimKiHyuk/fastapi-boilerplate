from fastapi.testclient import TestClient
from ..app import app


class TestService(object):
    def __new__(cls):
        return TestClient(app=app)
