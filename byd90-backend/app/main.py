from fastapi import FastAPI
from app.core.database import init_db
from app.api.auth import auth_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to BYD90 API"}
