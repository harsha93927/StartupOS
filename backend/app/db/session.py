from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Default to SQLite for local development, can be overridden by environment
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./startupos.db")

# pgvector would typically use postgresql://...
# For a production-grade system, we use a URL starting with postgresql://

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
