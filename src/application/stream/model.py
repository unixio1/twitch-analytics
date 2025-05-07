"""Stream models"""

from pydantic import BaseModel


class StreamDTO(BaseModel):
    """Stream data transfer object"""

    title: str
    user_name: str
