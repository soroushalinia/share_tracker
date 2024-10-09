"""
schema.py

This module defines data models for mongodb.
"""

from beanie import Document, Link
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone
from typing import List, Literal, Optional
from typing_extensions import Annotated


class User(Document):
  name: str
  username: str
  password: str
  email: EmailStr
  image: Optional[str] = Field(default=None)
  card_number: Optional[str] = Field(default=None)


class Request(BaseModel):
  username: str
  status: Literal["pending", "accepted", "declined"]


class Meeting(Document):
  date: Annotated[
    Optional[datetime],
    Field(default_factory=lambda: datetime.now(timezone.utc)),
  ]
  description: str
  members: Annotated[List[Link[User]], Field(default_factory=list)]
  creator: Link[User]
  requests: Annotated[List[Request], Field(default_factory=list)]


class Item(Document):
  name: str
  price: Optional[int] = Field(default=None)
  meeting: Link[Meeting]


class Order(Document):
  item: Item
  quantity: int
  users: Annotated[List[Link[User]], Field(default_factory=list)]
  meeting: Link[Meeting]


class Payment(Document):
  payed_by: Link[User]
  amount: int
  items: Annotated[List[Link[Item]], Field(default_factory=list)]
  meeting: Link[Meeting]


class Transaction(Document):
  user: User
  verified_by_owner: bool
  verified_by_user: bool
  amount: int
  received: bool
  meeting: Link[Meeting]


class Bill(Document):
  user: Link[User]
  amount: int
  negative: bool
  transactions: Annotated[List[Link[Transaction]], Field(default_factory=list)]
  meeting: Link[Meeting]
