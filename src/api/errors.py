"""API errors module"""

from pydantic import BaseModel


class BaseError(BaseModel):
    """Base API error"""

    message: str
