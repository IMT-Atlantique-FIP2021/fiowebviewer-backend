from starlette.testclient import TestClient
from backend.main import app
import pytest


@pytest.fixture
def client():
    return TestClient(app)


# TODO: Add fixture create "db" before all
# TODO: Add fixture delete "db" after all
