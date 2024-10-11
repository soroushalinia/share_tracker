from typing import Dict
from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
import pytest
from src.auth.model import User


@pytest.fixture
def anyio_backend() -> str:
  return "asyncio"


@pytest.fixture
async def mock_mongo(scope="session"):
  client = AsyncMongoMockClient()
  await init_beanie(
    document_models=[User], database=client.get_database(name="test_db")
  )


@pytest.fixture
async def mock_user(scope="session") -> Dict[str, str]:
  return {
    "username": "johndoe",
    "password": "password@123456",
    "email": "johndoe@mail.com",
    "name": "John Doe",
  }
