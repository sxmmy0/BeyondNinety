import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def init_db(retries: int = 10, delay: int = 3):
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("✅ Database initialized.")
            break
        except Exception as e:
            print(f"❌ DB connection failed (attempt {attempt+1}/{retries}) — retrying in {delay}s...")
            await asyncio.sleep(delay)
    else:
        raise Exception("🚨 Database failed to initialize after several attempts.")
