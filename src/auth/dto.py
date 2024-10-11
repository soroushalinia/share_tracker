"""
dto.py

Defines Data Transfer Objects (DTOs) for auth service.
"""

from beanie import PydanticObjectId
from pydantic import BaseModel


class RegisterRequestDto(BaseModel):
  name: str
  username: str
  email: str
  password: str


class RegisterResponseDto(BaseModel):
  id: PydanticObjectId
  name: str
  username: str
  email: str
