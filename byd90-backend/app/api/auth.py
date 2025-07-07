from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.core.security import hash_password, verify_password, create_access_token
from app.core.database import SessionLocal

auth_router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@auth_router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hash_password(user.password),
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@auth_router.post("/login")
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == credentials.email))
    user = result.scalars().first()

    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
