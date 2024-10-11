"""
service.py

Contains the AuthService class which is responsible
for user authentication and management.
"""

from typing import Optional
from fastapi import Depends
from src.auth import dto
from src.auth.interface import AuthServiceInterface, UserRepositoryInterface
from src.auth.repository import UserRepository
from src.auth.model import User
from src.util.security import PasswordContext


class AuthService(AuthServiceInterface):
  """Handles authentication and user management logic."""

  def __init__(
    self,
    password_context: PasswordContext = Depends(),
    user_repository: UserRepositoryInterface = Depends(UserRepository),
  ):
    super().__init__(password_context, user_repository)

  async def register_user(self, request: dto.RegisterRequestDto) -> User:
    existing_user: Optional[User] = await self._user_repository.find_user(
      email=request.email, username=request.username
    )
    if existing_user is not None:
      raise ValueError()

    hashed_password = self._password_context.hash_password(request.password)
    user = User(
      username=request.username,
      name=request.name,
      email=request.email,
      password=hashed_password,
    )
    new_user: User = await self._user_repository.create(user)
    return new_user
