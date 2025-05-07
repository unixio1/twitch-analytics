from typing import Iterator
from unittest import mock

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.api import setup_api
from src.settings import Settings, get_settings
from tests.infrastructure.twitch_api_stub import get_twitch_streams, get_user_by_id


@pytest.fixture
def api_client_mock(settings_mock: Settings) -> Iterator[TestClient]:
    """Test api client"""

    api = setup_api()

    def get_settings_mock() -> Settings:
        return settings_mock

    dependencies = {get_settings: get_settings_mock}
    api.dependency_overrides.update(dependencies)
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
