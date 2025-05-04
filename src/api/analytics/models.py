"Analytics endpoints models"

from pydantic import BaseModel


class GetUserOutput(BaseModel):
    """Output model for the get user endpoint"""
