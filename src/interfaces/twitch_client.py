"""Twitch client interface"""

from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import AsyncIterator

from httpx import AsyncClient


class ITwitchClient(ABC):
    @asynccontextmanager
    @abstractmethod
    def get_api_client() -> AsyncIterator[AsyncClient]:
        """Get the twitch client"""
