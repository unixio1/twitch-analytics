"""Main streams queries module"""

from typing import List

from httpx import HTTPError

from src.application import errors
from src.application.stream.model import StreamDTO
from src.infrastructure.stream import get_twitch_streams
from src.settings import Settings


async def get_streams(settings: Settings) -> List[StreamDTO]:
    """Main get stream query"""
    try:
        return await get_twitch_streams(settings)
    except HTTPError:
        raise errors.UnexpectedError("Internal server error")
