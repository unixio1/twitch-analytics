import uuid

import pytest

from src.settings import Settings


def test_settings(monkeypatch: pytest.MonkeyPatch):
    client_id = str(uuid.uuid4())
    client_secret = str(uuid.uuid4())
    monkeypatch.setenv("CLIENT_ID", client_id)
    monkeypatch.setenv("CLIENT_SECRET", client_secret)
    settings = Settings()
    assert settings.client_id == client_id
    assert settings.client_secret == client_secret
