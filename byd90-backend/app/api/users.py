from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse
from app.models.user import User
from app.core.dependencies import get_current_user

user_router = APIRouter()

@user_router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
