from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    region = Column(String, nullable=True)
