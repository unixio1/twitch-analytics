from datetime import datetime

import pytest

from src.application.user.model import UserDTO

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


@pytest.fixture
def user_mock() -> UserDTO:
    return USER_MOCK
