import pytest


class MockInsertOneResult:
    inserted_id: int = 1


# @pytest.fixture
async def mock_insert_one(
    database: str = "default", collection: str = "default", data: dict = {}
) -> MockInsertOneResult:
    # refactor |
    # check result of mongodb and return it with data
    return MockInsertOneResult()


# @pytest.fixture
async def mock_find_one(
    database: str = "default", collection: str = "default", data: dict = {}
):
    # refactor |
    # check result of mongodb and return it with data
    return {"inserted_id": 1, "some_property": 10}
