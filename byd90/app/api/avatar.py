from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.avatar import Avatar
from app.models.user import User
from app.schemas.avatar import AvatarCreate, AvatarResponse
from app.core.dependencies import get_current_user, get_db

avatar_router = APIRouter()

@avatar_router.post("/", response_model=AvatarResponse)
async def create_avatar(avatar: AvatarCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_avatar = Avatar(name=avatar.name, user_id=current_user.id)
    db.add(new_avatar)
    await db.commit()
    await db.refresh(new_avatar)
    return new_avatar

@avatar_router.get("/", response_model=AvatarResponse)
async def get_avatar(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Avatar).where(Avatar.user_id == current_user.id))
    avatar = result.scalars().first()
    if not avatar:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return avatar
