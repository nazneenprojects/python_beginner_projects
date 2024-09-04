"""
 Fast API Project : Digital Auto Market REST API Endpoint project

How to Run?
fastapi dev main.py

Output?
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

"""
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker



app = FastAPI()

# Include the user API router
app.include_router(user_router)

@app.get("/")
async def root(token: Annotated[str, Depends(get_current_active_user)]):
    return {"greet": "Guten Morgen, Champ! Your token is:", "token": token}