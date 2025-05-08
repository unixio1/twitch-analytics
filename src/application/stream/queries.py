"""Main streams queries module"""

from typing import List

from httpx import HTTPError

from src.application import errors
from src.application.stream.model import StreamDTO
from src.infrastructure.stream import get_twitch_streams
from src.interfaces.twitch_client import ITwitchClient


async def get_streams(twitch_client: ITwitchClient) -> List[StreamDTO]:
    """Main get stream query"""
    try:
        return await get_twitch_streams(twitch_client)
    except HTTPError:
        raise errors.UnexpectedError("Internal server error")
