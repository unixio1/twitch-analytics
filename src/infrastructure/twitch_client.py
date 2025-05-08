"""Twitch api client class"""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from httpx import AsyncClient, HTTPError

from src.interfaces.twitch_client import ITwitchClient


class TwitchClient(ITwitchClient):
    def __init__(self, client_id: str, client_secret: str):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__api_token = None

    @asynccontextmanager
    async def get_api_client(self) -> AsyncIterator[AsyncClient]:
        """Get the API http client"""
        await self.get_twitch_token()
        headers = {
            "Authorization": f"Bearer {self.__api_token}",
            "Client-Id": self.__client_id,
        }
        async with AsyncClient(headers=headers) as client:
            yield client

    async def get_twitch_token(self) -> None:
        """If not set or invalid, get a new twitch token"""
        is_valid_token = await self.__is_valid_token()
        if not is_valid_token:
            await self.__retrieve_twitch_token()

    async def __retrieve_twitch_token(self) -> str:
        """Retrieve the twitch token from the twitch API"""
        url = "https://id.twitch.tv/oauth2/token"
        data = {
            "client_id": self.__client_id,
            "client_secret": self.__client_secret,
            "grant_type": "client_credentials",
        }
        client: AsyncClient
        async with AsyncClient() as client:
            response = await client.post(url, data=data)
            data = response.json()
            self.__api_token = data["access_token"]

    async def __is_valid_token(self) -> bool:
        if not self.__api_token:
            return False
        url = "https://id.twitch.tv/oauth2/validate"
        headers = {"Authorization": f"OAuth {self.__api_token}"}
        async with AsyncClient(headers=headers) as client:
            response = await client.get(url)
            try:
                response.raise_for_status()
                return True
            except HTTPError:
                return False
