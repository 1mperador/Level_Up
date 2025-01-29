from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Substitua com o URL do seu banco de dados

# Configuração do engine e sessionmaker
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de declarações para os modelos
Base = declarative_base()

def init_db():
    """Inicializa o banco de dados criando todas as tabelas."""
    Base.metadata.create_all(bind=engine)

# A função `get_db` pode ser uma boa opção para criar a sessão no contexto da aplicação
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
