from sqlalchemy import Column, Integer, String, Float
from .database import Base  # Importação relativa

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(Integer, default=1)
    health = Column(Float, default=100.0)
    strength = Column(Float, default=10.0)
    intelligence = Column(Float, default=10.0)
