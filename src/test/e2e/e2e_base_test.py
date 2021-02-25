from ..initialize import TestService

client = TestService()


def test_service_available():
    res = client.get("/")
    assert res.status_code == 200
