"""
Application entry point
"""

import uvicorn

from src.api import setup_api
from src.settings import Settings


def main() -> None:
    """
    Main application entry point
    exposing the API
    """
    application_settings = Settings()
    uvicorn.run(
        setup_api,
        factory=True,
        host=application_settings.api_host_ip,
        port=application_settings.api_host_port,
    )


if __name__ == "__main__":
    main()
