from typing import Any, AsyncGenerator, Dict
from fastapi import FastAPI
import pytest
from httpx import ASGITransport, AsyncClient


@pytest.fixture
async def create_user(
  mock_user: Dict[str, str], app: FastAPI
) -> AsyncGenerator[Dict[str, Any], None]:
  async with AsyncClient(
    transport=ASGITransport(app=app), base_url="https://test"
  ) as ac:
    response = await ac.post("/auth/register", json=mock_user)
    yield {
      "status_code": response.status_code,
      "json": response.json(),
    }


@pytest.mark.anyio
async def test_user_register(create_user: Dict[str, Any]) -> None:
  assert create_user["status_code"] == 201
  response_data = create_user["json"]
  assert response_data["id"] is not None
  assert response_data["username"] == "johndoe"
  assert response_data["name"] == "John Doe"
  assert response_data["email"] == "johndoe@mail.com"


@pytest.mark.anyio
async def test_user_register_exists(app: FastAPI) -> None:
  async with AsyncClient(
    transport=ASGITransport(app=app), base_url="https://test"
  ) as ac:
    response = await ac.post(
      "/auth/register",
      json={
        "username": "johndoe",
        "name": "John Doe",
        "email": "johndoe@mail.com",
        "password": "password@123456",
      },
    )
  assert response.status_code == 409
  response_data = response.json()
  assert response_data == {"detail": "User with email/username already exists"}
