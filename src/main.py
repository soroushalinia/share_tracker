# pylint: disable=missing-module-docstring
from typing import AsyncIterator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .middleware.security import SecureHeadersMiddleware

from src.util.settings import Settings
from .util.database import init_db
from contextlib import asynccontextmanager

settings = Settings()  # type: ignore


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
  await init_db(settings.mongo_uri)
  yield


app: FastAPI = FastAPI(lifespan=lifespan)

# Middlewares
app.add_middleware(SecureHeadersMiddleware)
app.add_middleware(
  CORSMiddleware,
  allow_origins=settings.cors_origins.split(","),
  allow_credentials=True,
  allow_methods=["GET", "POST", "PUT", "DELETE"],
  allow_headers=["*"],
)
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)
app.add_middleware(
  TrustedHostMiddleware, allowed_hosts=settings.allowed_hosts.split(",")
)


@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
  return {"message": "OK"}
