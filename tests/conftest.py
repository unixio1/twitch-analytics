import pytest

from src.application.user.model import UserDTO
from tests.infrastructure.twitch_api_stub import get_user_by_id


@pytest.fixture
def user_mock() -> UserDTO:
    return get_user_by_id()
