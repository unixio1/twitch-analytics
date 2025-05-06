"""Twitch API client stub module"""

from src.application.user.model import UserDTO
from src.settings import Settings
from tests.conftest import USER_MOCK


async def get_user_by_id(id: int, settings: Settings) -> UserDTO:
    return USER_MOCK
