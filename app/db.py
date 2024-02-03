from app.settings import DB_CONNECTION_STRING
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(DB_CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, engine=engine)

class Base(DeclarativeBase):
    pass

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
