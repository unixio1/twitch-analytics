"""Main infrastructure module"""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from httpx import AsyncClient

from src.settings import Settings


@asynccontextmanager
async def get_api_client(settings: Settings) -> AsyncIterator[AsyncClient]:
    """Get the API http client"""
    twitch_token = await get_twitch_token(settings.client_id, settings.client_secret)
    headers = {
        "Authorization": f"Bearer {twitch_token}",
        "Client-Id": settings.client_id,
    }
    async with AsyncClient(headers=headers) as client:
        yield client


async def get_twitch_token(client_id: str, client_secret: str) -> str:
    """Get the twitch api token"""
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    client: AsyncClient
    async with AsyncClient() as client:
        response = await client.post(url, data=data)
        data = response.json()
        return data["access_token"]
