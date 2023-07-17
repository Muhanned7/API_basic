from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import setting

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}/{setting.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
while True:

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastApi",
            user="postgres",
            password="123",
            cursor_factory=RealDictCursor,
        )

        cursor = conn.cursor()
        print("Database connect was connected")
        break
    except Exception as error:
        print("connecting the database failed")
        print("error", error)
        time.sleep(2)
"""
