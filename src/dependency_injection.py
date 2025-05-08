"""Dependency injection module"""

from src.infrastructure.twitch_client import TwitchClient
from src.interfaces.twitch_client import ITwitchClient
from src.settings import get_settings

TWITCH_CLIENT = TwitchClient(get_settings().client_id, get_settings().client_secret)


def get_twitch_client() -> ITwitchClient:
    """Get the twitch api client"""
    return TWITCH_CLIENT
