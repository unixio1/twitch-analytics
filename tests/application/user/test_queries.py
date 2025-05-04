"""Test user queries"""

import pytest

from src.application.user.model import UserDTO
from src.application.user.queries import get_user


@pytest.mark.asyncio
async def test_get_user(user_mock: UserDTO) -> None:
    "Test get user"
    fetched_user = await get_user(user_mock.id)
    assert fetched_user == user_mock
