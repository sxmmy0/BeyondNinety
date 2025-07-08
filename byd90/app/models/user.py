from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # New onboarding fields
    full_name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    location = Column(String, nullable=True)        # e.g. "London, UK"
    position = Column(String, nullable=True)        # e.g. "Midfielder"
    training_focus = Column(String, nullable=True)  # e.g. "Fitness, Recovery"
    favourite_team = Column(String, nullable=True)  # e.g. "Arsenal"
    current_team = Column(String, nullable=True)    # e.g. "Free Agent"
    avatar_name = Column(String, nullable=True)     # e.g. "Zion"
    avatar = relationship("Avatar", back_populates="user", uselist=False)

