"""Twitch API client stub module"""

from datetime import datetime
from typing import AsyncIterator, List

from httpx import AsyncClient

from src.application.stream.model import StreamDTO
from src.application.user.model import UserDTO
from src.interfaces.twitch_client import ITwitchClient

USER_MOCK = UserDTO(
    id="123",
    login="user",
    display_name="User",
    type="",
    broadcaster_type="partner",
    description="Description",
    profile_image_url="",
    offline_image_url="",
    view_count=0,
    created_at=datetime.fromisoformat("2020-01-01T00:00:00Z"),
)

STREAM_MOCK = StreamDTO(title="Sample stream", user_name="Some user")


class TwitchClientMock(ITwitchClient):
    def __init__(self, client_id: str, client_secret: str):
        pass

    async def get_api_client() -> AsyncIterator[AsyncClient]:
        pass


async def get_user_by_id(user_id: int, twitch_client: ITwitchClient) -> UserDTO:
    return USER_MOCK


async def get_twitch_streams(twitch_client: ITwitchClient) -> List[StreamDTO]:
    return [STREAM_MOCK]
