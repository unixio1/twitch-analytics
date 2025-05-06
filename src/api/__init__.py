import importlib

from fastapi import FastAPI

from src.api import error_handler
from src.api.analytics import analytics_router
from src.application import errors


def setup_api() -> FastAPI:
    """Setup the API"""

    api_version = importlib.metadata.version("twitch-analytics")
    api = FastAPI(title="Twitch analytics API", version=api_version)

    api.include_router(analytics_router, prefix="/analytics")

    api.add_exception_handler(errors.UnexpectedError, error_handler.internal_error)
    api.add_exception_handler(errors.ModelNotFoundError, error_handler.not_found)
    api.add_exception_handler(errors.InvalidTokenError, error_handler.unauthorized)
    api.add_exception_handler(errors.InvalidParameterError, error_handler.bad_request)
    return api
