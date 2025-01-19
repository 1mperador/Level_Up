from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    level: int
    health: float
    strength: float
    intelligence: float

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True
