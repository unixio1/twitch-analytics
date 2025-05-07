"""Twitch API client stub module"""

from typing import List

from src.application.stream.model import StreamDTO
from src.application.user.model import UserDTO
from src.settings import Settings
from tests.conftest import STREAM_MOCK, USER_MOCK


async def get_user_by_id(user_id: int, settings: Settings) -> UserDTO:
    return USER_MOCK


async def get_twitch_streams(settings: Settings) -> List[StreamDTO]:
    return [STREAM_MOCK]
