from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_game import crud, models
from fastapi_game.database import init_db, engine, database
# from . import crud, models
from . import schemas  # Importações relativas
# from .database import init_db, database

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/characters/", response_model=schemas.Character)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    return crud.create_character(db=db, character=character)

@app.get("/characters/", response_model=list[schemas.Character])
def get_characters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    characters = crud.get_characters(db=db, skip=skip, limit=limit)
    return characters

@app.get("/characters/{character_id}", response_model=schemas.Character)
def get_character(character_id: int, db: Session = Depends(get_db)):
    db_character = crud.get_character(db=db, character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

# init_db()