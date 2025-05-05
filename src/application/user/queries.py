"""Twitch user queries"""

from src.application.user.model import UserDTO
from src.infrastructure.user import get_user_by_id


async def get_user(user_id: int) -> UserDTO:
    """Get a twitch user data given the ID"""

    return await get_user_by_id(user_id)
