from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.coach import Coach
from app.core.dependencies import get_current_user, get_db
from app.schemas.coach import CoachResponse

coach_router = APIRouter()

@coach_router.get("/recommended", response_model=list[CoachResponse])
async def recommend_coaches(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    result = await db.execute(select(Coach).where(Coach.specialty.ilike(f"%{current_user.training_focus}%")))
    return result.scalars().all()
