"""Twitch Api client module"""

from typing import Optional

from httpx import AsyncClient

from src.application.user.model import UserDTO
from src.infrastructure import get_api_client
from src.settings import Settings


async def get_user_by_id(user_id: int) -> Optional[UserDTO]:
    settings = Settings()
    url = "https://api.twitch.tv/helix/users"
    query_parameters = {"id": user_id}
    client: AsyncClient
    async with get_api_client(settings) as client:
        response = await client.get(url, params=query_parameters)
        if response.status_code == 404:
            return None
        response = response.raise_for_status()
        data = response.json()
    return UserDTO(**data["data"][0])
