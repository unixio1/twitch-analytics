import uuid

import pytest

from src.settings import Settings


def test_settings(monkeypatch: pytest.MonkeyPatch):
    client_id = str(uuid.uuid4())
    client_secret = str(uuid.uuid4())
    api_host_ip = "0.0.0.0"
    api_host_port = "80"
    monkeypatch.setenv("CLIENT_ID", client_id)
    monkeypatch.setenv("CLIENT_SECRET", client_secret)
    monkeypatch.setenv("API_HOST_IP", api_host_ip)
    monkeypatch.setenv("API_HOST_PORT", api_host_port)
    settings = Settings()
    assert settings.client_id == client_id
    assert settings.client_secret == client_secret
    assert api_host_ip == api_host_ip
    assert settings.api_host_port == int(api_host_port)
