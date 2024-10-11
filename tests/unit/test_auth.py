from typing import AsyncGenerator
from bson import ObjectId
import pytest
from src.auth.dto import RegisterRequestDto
from src.auth.model import User
from src.auth.repository import UserRepository
from src.auth.service import AuthService
from src.util.security import PasswordContext


@pytest.fixture
async def mock_repo(mock_mongo) -> UserRepository:
  repo = UserRepository()
  return repo


@pytest.fixture
async def mock_password_context() -> PasswordContext:
  return PasswordContext()


@pytest.fixture
async def mock_new_user(mock_user) -> AsyncGenerator[User, None]:
  new_user = await User(**mock_user).create()
  yield new_user
  await new_user.delete()


@pytest.mark.anyio
async def test_repo_get_user(mock_repo, mock_new_user) -> None:
  user = await mock_repo.get_user(mock_new_user.id)
  assert user.id == mock_new_user.id
  assert user.username == mock_new_user.username
  assert user.name == mock_new_user.name
  assert user.email == mock_new_user.email
  assert user.password == mock_new_user.password


@pytest.mark.anyio
async def test_repo_find_user(mock_repo, mock_new_user) -> None:
  user = await mock_repo.find_user(mock_new_user.email, mock_new_user.username)
  assert user is not None


@pytest.mark.anyio
async def test_repo_create_user(mock_repo, mock_user) -> None:
  user = User(**mock_user)
  new_user = await mock_repo.create(user)
  created_user = await User.get(new_user.id)
  assert created_user is not None
  await created_user.delete()


@pytest.mark.anyio
async def test_service_create_user(
  mock_repo, mock_password_context, mock_user
) -> None:
  service = AuthService(mock_password_context, mock_repo)
  user = await service.register_user(RegisterRequestDto(**mock_user))
  assert ObjectId.is_valid(user.id)
  assert mock_password_context.verify_password(
    mock_user["password"], user.password
  )


@pytest.mark.anyio
async def test_service_create_existing_user(
  mock_repo, mock_password_context, mock_user, mock_new_user
) -> None:
  service = AuthService(mock_password_context, mock_repo)
  with pytest.raises(ValueError):
    await service.register_user(RegisterRequestDto(**mock_user))
