"""Twitch Api client module"""

from typing import Optional

from httpx import AsyncClient

from src.application.user.model import UserDTO
from src.interfaces.twitch_client import ITwitchClient


async def get_user_by_id(
    user_id: int, twitch_client: ITwitchClient
) -> Optional[UserDTO]:
    url = "https://api.twitch.tv/helix/users"
    query_parameters = {"id": user_id}
    client: AsyncClient
    async with twitch_client.get_api_client() as client:
        response = await client.get(url, params=query_parameters)
        if response.status_code == 404:
            return None
        response = response.raise_for_status()
        data = response.json()
    return UserDTO(**data["data"][0])
