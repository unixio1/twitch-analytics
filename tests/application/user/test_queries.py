"""Test user queries"""

from unittest import mock

import pytest

from src.application.user.model import UserDTO
from src.application.user.queries import get_user
from tests.infrastructure.twitch_api_stub import get_user_by_id


@mock.patch("src.application.user.queries.get_user_by_id", get_user_by_id)
@pytest.mark.asyncio
async def test_get_user(user_mock: UserDTO) -> None:
    "Test get user"
    fetched_user = await get_user(user_mock.id)
    assert fetched_user == user_mock
