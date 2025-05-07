from datetime import datetime
from typing import List

import pytest

from src.application.stream.model import StreamDTO
from src.application.user.model import UserDTO
from src.settings import Settings

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


@pytest.fixture
def settings_mock(monkeypatch: pytest.MonkeyPatch) -> Settings:
    monkeypatch.setenv("CLIENT_ID", "Test client")
    monkeypatch.setenv("CLIENT_SECRET", "Test secret")
    return Settings()


@pytest.fixture
def user_mock() -> UserDTO:
    return USER_MOCK


@pytest.fixture
def streams_mock() -> List[StreamDTO]:
    return [STREAM_MOCK]
