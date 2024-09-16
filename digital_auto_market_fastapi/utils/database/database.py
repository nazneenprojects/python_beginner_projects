import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("/home/zermatt/Documents/python_beginner_projects/digital_auto_market_fastapi/.env")

# Retrieve environment variables
db_name = os.getenv("DB_NAME")
db_server = os.getenv("DB_SERVER")
db_uid = os.getenv("DB_UID")
db_pw = os.getenv("DB_PWD")

# Verify environment variables
if not db_uid or not db_pw:
    raise ValueError("Database user ID or password not set in .env file.")

# Construct connection string
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc:///?odbc_connect=" + quote_plus(
        "Driver={ODBC Driver 17 for SQL Server};"
        f"Server=tcp:{db_server},1433;"
        f"Database={db_name};"
        f"Uid={db_uid};"
        f"Pwd={db_pw};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
# Base is an instance of declarative_base() (from SQLAlchemy) that serves as a foundation for defining the ORM models (tables).
# All models (such as User, AutoInfo, etc.) inherit from this Base class.
Base = declarative_base()
