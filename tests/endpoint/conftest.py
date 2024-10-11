import os
from typing import Dict, Generator
from fastapi import FastAPI
import pytest
from testcontainers.mongodb import MongoDbContainer

from src.util.database import init_db


@pytest.fixture
def anyio_backend() -> str:
  return "asyncio"


@pytest.fixture(scope="session")
def mongo_container() -> Generator[MongoDbContainer, None, None]:
  container: MongoDbContainer = MongoDbContainer("mongo:8.0-noble")
  container.start()
  uri: str = container.get_connection_url()
  os.environ["MONGO_URI"] = uri
  yield container
  container.stop()


@pytest.fixture()
async def app(mongo_container: MongoDbContainer) -> FastAPI:
  os.environ["CORS_ORIGINS"] = "*"
  os.environ["ALLOWED_HOSTS"] = "*"
  from src.main import app, lifespan

  async with lifespan(app):
    return app


@pytest.fixture
def mock_user() -> Dict[str, str]:
  return {
    "username": "johndoe",
    "password": "password@123456",
    "email": "johndoe@mail.com",
    "name": "John Doe",
  }
