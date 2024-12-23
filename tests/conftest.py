import pytest
from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True
    UPLOAD_FOLDER = Config.BASE_DIR / 'test_storage'

@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()