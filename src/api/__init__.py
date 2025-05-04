import importlib

from fastapi import FastAPI

from src.api.analytics import analytics_router


def setup_api() -> FastAPI:
    """Setup the API"""

    api_version = importlib.metadata.version("twitch-analytics")
    api = FastAPI(title="Twitch analytics API", version=api_version)

    api.include_router(analytics_router, prefix="/analytics")
    return api
