"""Application errors"""


class BasicApplicationError(Exception):
    """Base application error"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidParameterError(BasicApplicationError):
    """Error when the query contains an invalid id"""


class ModelNotFoundError(BasicApplicationError):
    """User not found error"""


class InvalidTokenError(BasicApplicationError):
    """Invalid token error"""


class UnexpectedError(BasicApplicationError):
    """Unexpected error"""
