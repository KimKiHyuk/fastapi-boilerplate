from ..initialize import Test

client = Test()


def test_service_available():
    res = client.get("/")
    assert res.status_code == 200
