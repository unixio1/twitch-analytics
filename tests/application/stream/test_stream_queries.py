"""Test stream queries"""

from typing import List
from unittest import mock

import pytest

from src.application.stream.model import StreamDTO
from src.application.stream.queries import get_streams
from src.interfaces.twitch_client import ITwitchClient
from tests.infrastructure.twitch_api_stub import get_twitch_streams


@mock.patch("src.application.stream.queries.get_twitch_streams", get_twitch_streams)
@pytest.mark.asyncio
async def test_get_streams(
    streams_mock: List[StreamDTO], twitch_client_mock: ITwitchClient
):
    """Test main stream query"""
    streams = await get_streams(twitch_client_mock)
    assert streams_mock == streams
