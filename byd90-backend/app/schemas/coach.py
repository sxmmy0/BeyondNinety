from pydantic import BaseModel

class CoachResponse(BaseModel):
    id: int
    name: str
    specialty: str
    region: str | None

    class Config:
        from_attributes = True
