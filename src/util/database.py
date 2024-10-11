"""
database.py

This module initializes the MongoDB database connection.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.auth.model import User


async def init_db(mongo_uri: str) -> None:
  db: AsyncIOMotorClient = AsyncIOMotorClient(mongo_uri)
  await init_beanie(
    database=db.share_tracker,
    document_models=[User],
  )
