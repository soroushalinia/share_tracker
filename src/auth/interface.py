"""
interface.py

Defines abstract interfaces for user repository and authentication service.
"""

from typing import Optional
from abc import ABC, abstractmethod

from beanie import PydanticObjectId
from src.auth.model import User
from src.auth import dto
from src.util.security import PasswordContext


class UserRepositoryInterface(ABC):
  @abstractmethod
  async def find_user(self, email: str, username: str) -> Optional[User]:
    pass  # pragma: no cover

  @abstractmethod
  async def create(self, user: User) -> User:
    pass  # pragma: no cover

  async def get_user(self, user_id: PydanticObjectId) -> Optional[User]:
    pass  # pragma: no cover


class AuthServiceInterface(ABC):
  def __init__(
    self,
    password_context: PasswordContext,
    user_repository: UserRepositoryInterface,
  ):
    self._password_context = password_context
    self._user_repository = user_repository

  @abstractmethod
  async def register_user(self, request: dto.RegisterRequestDto) -> User:
    pass  # pragma: no cover
