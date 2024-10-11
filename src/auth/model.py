"""
model.py

Defines the MongoDB schema for the User model,
used for database representation and validation.
"""

from typing import Optional
from beanie import Document
from pydantic import EmailStr, Field


class User(Document):
  name: str
  username: str
  password: str
  email: EmailStr
  image: Optional[str] = Field(default=None)
  card_number: Optional[str] = Field(default=None)
