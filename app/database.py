# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the database URL from the environment
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

# Create engine and session maker
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # for SQLite, remove `connect_args` if using other DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
