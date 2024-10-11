"""
auth.py

This module handles routing for auth related actions in the API.
"""

from fastapi import APIRouter, Depends
from fastapi import HTTPException, status

from src.auth.interface import AuthServiceInterface
from src.auth.service import AuthService
from src.auth import dto
from src.auth.model import User

router = APIRouter()


@router.post(
  "/register",
  response_model=dto.RegisterResponseDto,
  responses={
    409: {
      "description": "User with email/username already exists",
      "content": {
        "application/json": {
          "example": {"detail": "User with email/username already exists"}
        }
      },
    },
    201: {
      "description": "User created successfully",
      "content": {
        "application/json": {
          "example": {
            "id": "123",
            "name": "John",
            "email": "john@example.com",
            "username": "john",
          }
        }
      },
    },
  },
  status_code=status.HTTP_201_CREATED,
)
async def register_user(
  request: dto.RegisterRequestDto,
  auth_service: AuthServiceInterface = Depends(AuthService),
):
  try:
    user: User = await auth_service.register_user(request)
    assert user.id is not None
    return dto.RegisterResponseDto(
      id=user.id, username=user.username, name=user.name, email=user.email
    )
  except ValueError as exc:
    raise HTTPException(
      status_code=409, detail="User with email/username already exists"
    ) from exc
