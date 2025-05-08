"""Streams related infrastructure module"""

from typing import List

from httpx import AsyncClient

from src.application.stream.model import StreamDTO
from src.interfaces.twitch_client import ITwitchClient


async def get_twitch_streams(twitch_client: ITwitchClient) -> List[StreamDTO]:
    """Get a list of twitch streams"""
    url = "https://api.twitch.tv/helix/streams"
    client: AsyncClient
    async with twitch_client.get_api_client() as client:
        response = await client.get(url)
        if response.status_code == 404:
            return []
        response = response.raise_for_status()
        data = response.json()
        return [StreamDTO(**stream) for stream in data["data"]]
    return
