import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/galinaceos"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def init_db():
    """Cria as tabelas no banco, caso ainda não existam."""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Abre uma sessão com o banco de dados."""
    return SessionLocal()
