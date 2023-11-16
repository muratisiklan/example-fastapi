from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f"mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Run hard coded sql if not to prefer using sql alchemy
# import mysql.connector
# import time
# connection_info = {
#     "host": "localh
#     "user": "r
#     "password": "Ne
#     "database": "fast
# }


# while True:

#     try:
#         conn = mysql.connector.connect(**connection_info)
#         cursor = conn.cursor(dictionary=True)
#         print("Succesfuly connected")
#         break

#     except Exception as e:
#         print("Connection Failed")
#         print("Error:", e)
#         time.sleep(4)
