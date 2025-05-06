"""Error handler module"""

from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.api.errors import BaseError
from src.application import errors


def internal_error(_request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, errors.UnexpectedError)

    return JSONResponse(
        content=BaseError(message=exc.message).model_dump(),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def not_found(_request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, errors.ModelNotFoundError)

    return JSONResponse(
        content=BaseError(message=exc.message).model_dump(),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


def unauthorized(_request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, errors.InvalidTokenError)

    return JSONResponse(
        content=BaseError(message=exc.message).model_dump(),
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


def bad_request(_request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, errors.InvalidParameterError)

    return JSONResponse(
        content=BaseError(message=exc.message).model_dump(),
        status_code=status.HTTP_400_BAD_REQUEST,
    )
