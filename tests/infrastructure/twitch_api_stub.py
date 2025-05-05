"""Twitch API client stub module"""

from src.application.user.model import UserDTO
from tests.conftest import USER_MOCK


async def get_user_by_id(id: int = 0) -> UserDTO:
    return USER_MOCK
