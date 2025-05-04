from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    client_id: str
    client_secret: str
    api_host_ip: str = "127.0.0.1"
    api_host_port: int = 8080

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
