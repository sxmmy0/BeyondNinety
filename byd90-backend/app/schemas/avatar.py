from pydantic import BaseModel

class AvatarCreate(BaseModel):
    name: str

class AvatarResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
