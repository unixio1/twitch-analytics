"""Test user queries"""

from unittest import mock

import pytest

from src.application import errors
from src.application.user.model import UserDTO
from src.application.user.queries import get_user
from src.interfaces.twitch_client import ITwitchClient
from tests.infrastructure.twitch_api_stub import get_user_by_id


@mock.patch("src.application.user.queries.get_user_by_id", get_user_by_id)
@pytest.mark.asyncio
async def test_get_user(user_mock: UserDTO, twitch_client_mock: ITwitchClient) -> None:
    "Test get user"
    fetched_user = await get_user(int(user_mock.id), twitch_client_mock)
    assert fetched_user == user_mock


@mock.patch("src.application.user.queries.get_user_by_id", get_user_by_id)
@pytest.mark.asyncio
async def test_get_user_invalid_id(twitch_client_mock: ITwitchClient) -> None:
    """Test get user with invalid id"""
    with pytest.raises(errors.InvalidParameterError):
        await get_user(-1, twitch_client_mock)
