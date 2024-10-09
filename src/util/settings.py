"""
settings.py

This modules providee setting class to get secrets and credentials
from enviroment variables using pydantic.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  mongo_uri: str
  cors_origins: str
  allowed_hosts: str
