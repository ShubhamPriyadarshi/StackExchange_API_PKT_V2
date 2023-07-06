import pandas as pd
from sqlalchemy import create_engine
from app.core.config import key,snowflake_user,snowflake_account,snowflake_schema,snowflake_warehouse,snowflake_database,snowflake_password

SNOWFLAKE_ACCOUNT = snowflake_account
SNOWFLAKE_USER = snowflake_user
SNOWFLAKE_PASSWORD = snowflake_password
SNOWFLAKE_WAREHOUSE = snowflake_warehouse
SNOWFLAKE_DATABASE = snowflake_database
SNOWFLAKE_SCHEMA = snowflake_schema

DATABASE_URL = (
    f"snowflake://{SNOWFLAKE_USER}:{SNOWFLAKE_PASSWORD}@{SNOWFLAKE_ACCOUNT}/"
    f"{SNOWFLAKE_DATABASE}/{SNOWFLAKE_SCHEMA}?warehouse={SNOWFLAKE_WAREHOUSE}&role=WRITER"
)

engine = create_engine(DATABASE_URL)

class SnowflakeService:
    @staticmethod
    def insert_data_from_csv(csv_file):
        with engine.begin() as conn:
            for chunk in pd.read_csv(csv_file, chunksize=10000, header=None):
                chunk.columns = ['name', 'count', 'ingestion_timestamp']
                chunk.to_sql("tags", conn, if_exists="append", index=False)
