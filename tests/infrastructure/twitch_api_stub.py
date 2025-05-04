"""Twitch API client stub module"""

import datetime

from src.application.user.model import UserDTO


def get_user_by_id() -> UserDTO:
    return UserDTO(
        id="123",
        login="user",
        display_name="User",
        type="",
        broadcaster_type="partner",
        description="Description",
        profile_image_url="",
        offline_image_url="",
        view_count=0,
        created_at=datetime.datetime.fromisoformat("2020-01-01T00:00:00Z"),
    )
