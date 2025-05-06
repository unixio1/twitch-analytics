"""Twitch analytics related endpoints"""

import fastapi

from src.api.analytics.models import GetUserOutput
from src.api.errors import BaseError
from src.application.user import queries

analytics_router = fastapi.APIRouter()


@analytics_router.get(
    "/user",
    status_code=fastapi.status.HTTP_200_OK,
    responses={
        fastapi.status.HTTP_400_BAD_REQUEST: {"model": BaseError},
        fastapi.status.HTTP_401_UNAUTHORIZED: {"model": BaseError},
        fastapi.status.HTTP_404_NOT_FOUND: {"model": BaseError},
        fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": BaseError},
    },
)
async def get_user(id: int) -> GetUserOutput:
    """Get a twitch user"""
    user = await queries.get_user(id)
    return GetUserOutput(user=user)
