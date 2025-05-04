from typing import Iterator

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.api import setup_api


@pytest.fixture
def api_client_mock() -> Iterator[TestClient]:
    """Test api client"""

    api = setup_api()
    yield TestClient(api)


def test_get_user(api_client_mock: TestClient) -> None:
    """Test get user endpoint"""

    endpoint = "/analytics/user?id=1"
    response = api_client_mock.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
