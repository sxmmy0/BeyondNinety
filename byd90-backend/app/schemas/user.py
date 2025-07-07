from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: str
    age: int
    location: str
    position: str
    training_focus: str
    favourite_team: str
    current_team: str
    avatar_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    full_name: str
    age: int
    location: str
    position: str
    training_focus: str
    favourite_team: str
    current_team: str
    avatar_name: str

    class Config:
        orm_mode = True
