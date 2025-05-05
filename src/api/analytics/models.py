"Analytics endpoints models"

from pydantic import BaseModel

from src.application.user.model import UserDTO


class GetUserOutput(BaseModel):
    """Output model for the get user endpoint"""

    user: UserDTO
