from fastapi import FastAPI
from app.core.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to BYD90 API"}
