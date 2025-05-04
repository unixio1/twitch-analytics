"""User application models"""

import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    """User data transfer object"""

    id: str
    login: str
    display_name: str
    type: str
    broadcaster_type: str
    description: str
    profile_image_url: str
    offline_image_url: str
    view_count: int
    created_at: datetime.datetime
