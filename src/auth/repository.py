"""
repository.py

Defines the UserRepository class for interacting with the user collection.
"""

from typing import Optional

from beanie import PydanticObjectId
from src.auth.model import User
from src.auth.interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
  """Repository for managing user data persistence in the database."""

  async def create(self, user: User) -> User:
    new_user = await user.create()
    return new_user

  async def find_user(self, email: str, username: str) -> Optional[User]:
    user = await User.find_one(
      {"$or": [{"email": email}, {"username": username}]}
    )
    return user

  async def get_user(self, user_id: PydanticObjectId) -> Optional[User]:
    return await User.get(id)
