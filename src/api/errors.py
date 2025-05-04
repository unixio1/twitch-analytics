"""API errors module"""

from fastapi import status
from pydantic import BaseModel


class BaseError(BaseModel):
    """Base API error"""

    message: str
    path: str


class BadRequest(BaseError):
    """Bad request api error"""

    error_code: int = status.HTTP_400_BAD_REQUEST


class Unauthorized(BaseError):
    """Unauthorized error"""

    error_code: int = status.HTTP_401_UNAUTHORIZED


class NotFound(BaseError):
    """Not found error"""

    error_code: int = status.HTTP_404_NOT_FOUND


class InternalServerError(BaseError):
    """Internal server error"""

    error_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
