from typing import List

import pytest

from src.application.stream.model import StreamDTO
from src.application.user.model import UserDTO
from src.interfaces.twitch_client import ITwitchClient
from src.settings import Settings
from tests.infrastructure.twitch_api_stub import (
    STREAM_MOCK,
    USER_MOCK,
    TwitchClientMock,
)


@pytest.fixture
def settings_mock(monkeypatch: pytest.MonkeyPatch) -> Settings:
    monkeypatch.setenv("CLIENT_ID", "Test client")
    monkeypatch.setenv("CLIENT_SECRET", "Test secret")
    return Settings()


@pytest.fixture
def twitch_client_mock(settings_mock: Settings) -> ITwitchClient:
    return TwitchClientMock(settings_mock.client_id, settings_mock.client_secret)


@pytest.fixture
def user_mock() -> UserDTO:
    return USER_MOCK


@pytest.fixture
def streams_mock() -> List[StreamDTO]:
    return [STREAM_MOCK]
