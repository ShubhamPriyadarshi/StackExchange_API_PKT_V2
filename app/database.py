from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import snowflake_account, snowflake_user, snowflake_password, snowflake_database, snowflake_schema
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
snowflake_url = f"snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/{snowflake_database}/{snowflake_schema}"

engine = create_engine(snowflake_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
