from database_connect import engine
from user_model import Base

Base.metadata.create_all(bind=engine)
