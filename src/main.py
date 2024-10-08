# pylint: disable=missing-module-docstring
from typing import AsyncIterator
from fastapi import FastAPI

from src.util.settings import Settings
from .util.database import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
  settings = Settings()
  await init_db(settings.mongo_uri)
  yield


app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
  return {"message": "OK"}
