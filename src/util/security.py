"""
security.py

This module provides the PasswordContext class, which handles password hashing
and verification using the bcrypt algorithm. It utilizes the Passlib library to
ensure secure password management in applications.
"""

from passlib.context import CryptContext


class PasswordContext:
  def __init__(self) -> None:
    self._context = CryptContext(schemes=["bcrypt"], deprecated="auto")

  def hash_password(self, password: str) -> str:
    return self._context.hash(password)

  def verify_password(self, plain_password: str, hashed_password: str) -> bool:
    return self._context.verify(plain_password, hashed_password)
