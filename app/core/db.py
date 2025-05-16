# app/core/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Замените на вашу строку подключения PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://mydb_rn9d_user:CApOS2v83SFaQVu3NyqV8LLKbmekZOmc@dpg-d0dlg11r0fns739cfh9g-a:5432/mydb_rn9d"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
