"""Test endpoints using fastapi test clientc"""

import os
from typing import Generator
from fastapi.testclient import TestClient
import pytest
from testcontainers.mongodb import MongoDbContainer
from src.main import app


@pytest.fixture(scope="session")
def mongo_container() -> Generator[MongoDbContainer, None, None]:
  container = MongoDbContainer("mongo:8.0-noble")
  container.start()
  uri = container.get_connection_url()
  os.environ["MONGO_URI"] = uri

  yield container
  container.stop()


@pytest.fixture()
def client(mongo_container: MongoDbContainer) -> TestClient:
  return TestClient(app)


def test_read_main(client: TestClient):
  response = client.get("/healthcheck")
  assert response.status_code == 200
  assert response.json() == {"message": "OK"}
