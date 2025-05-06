"""Twitch user queries"""

from httpx import HTTPError

from src.application import errors
from src.application.user.model import UserDTO
from src.infrastructure.user import get_user_by_id


async def get_user(user_id: int) -> UserDTO:
    """Get a twitch user data given the ID"""
    _raise_if_invalid_id(user_id)
    try:
        user = await get_user_by_id(user_id)
        if not user:
            raise errors.ModelNotFoundError("User not found")
        return user
    except HTTPError:
        raise errors.UnexpectedError("Internal server error")


def _raise_if_invalid_id(user_id: int) -> None:
    """Raise an error if the id is invalid"""
    if not isinstance(user_id, int) or user_id <= 0:
        raise errors.InvalidParameterError("Invalid or missing id parameter")
