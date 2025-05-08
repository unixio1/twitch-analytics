from typing import Iterator
from unittest import mock

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.api import setup_api
from tests.infrastructure.twitch_api_stub import get_twitch_streams, get_user_by_id


@pytest.fixture
def api_client_mock() -> Iterator[TestClient]:
    """Test api client"""

    api = setup_api()

    yield TestClient(api)


@mock.patch("src.api.analytics.queries.get_user", get_user_by_id)
def test_get_user(api_client_mock: TestClient) -> None:
    """Test get user endpoint"""

    endpoint = "/analytics/user?id=1"
    response = api_client_mock.get(endpoint)
    assert response.status_code == status.HTTP_200_OK


@mock.patch("src.api.analytics.get_streams", get_twitch_streams)
def test_get_streams(api_client_mock: TestClient) -> None:
    """Test get streams endpoint"""

    endpoint = "/analytics/streams"
    response = api_client_mock.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
