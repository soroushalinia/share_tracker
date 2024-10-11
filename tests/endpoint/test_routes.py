from fastapi import FastAPI
import pytest
from httpx import ASGITransport, AsyncClient


@pytest.mark.anyio
async def test_read_main(app: FastAPI) -> None:
  async with AsyncClient(
    transport=ASGITransport(app=app), base_url="https://test"
  ) as ac:
    response = await ac.get("/healthcheck")
  assert response.status_code == 200
  assert response.json() == {"message": "OK"}
