"""Twitch analytics related endpoints"""

import fastapi

from src.api import errors
from src.api.analytics.models import GetUserOutput

analytics_router = fastapi.APIRouter()


@analytics_router.get(
    "/user",
    status_code=fastapi.status.HTTP_200_OK,
    responses={
        fastapi.status.HTTP_400_BAD_REQUEST: {"model": errors.BadRequest},
        fastapi.status.HTTP_401_UNAUTHORIZED: {"model": errors.Unauthorized},
        fastapi.status.HTTP_404_NOT_FOUND: {"model": errors.NotFound},
        fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": errors.InternalServerError
        },
    },
)
async def get_user(id: int) -> GetUserOutput:
    """Get a twitch user"""

    return GetUserOutput()
