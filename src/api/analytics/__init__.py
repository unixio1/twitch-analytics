"""Twitch analytics related endpoints"""

import fastapi

from src.api.analytics.models import GetStreamsOutput, GetUserOutput
from src.api.errors import BaseError
from src.application.stream.queries import get_streams
from src.application.user import queries
from src.dependency_injection import get_twitch_client
from src.interfaces.twitch_client import ITwitchClient

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
async def get_user(
    id: int,
    twitch_client: ITwitchClient = fastapi.Depends(get_twitch_client),
) -> GetUserOutput:
    """Get a twitch user"""
    user = await queries.get_user(id, twitch_client)
    return GetUserOutput(user=user)


@analytics_router.get(
    "/streams",
    status_code=fastapi.status.HTTP_200_OK,
    responses={
        fastapi.status.HTTP_401_UNAUTHORIZED: {"model": BaseError},
        fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": BaseError},
    },
)
async def get_stream(
    twitch_client: ITwitchClient = fastapi.Depends(get_twitch_client),
) -> GetStreamsOutput:
    """Get twitch streams"""
    streams = await get_streams(twitch_client)
    return GetStreamsOutput(streams=streams)
