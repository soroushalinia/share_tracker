"""Setting class to get secrets and credentials from enviroment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  mongo_uri: str
