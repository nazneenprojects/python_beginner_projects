"""
 Fast API Project : Digital Auto Market REST API Endpoint project

How to Run?
fastapi dev main.py

Output?
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

"""
from typing import Annotated
from fastapi import FastAPI, Depends

from digital_auto_market_fastapi.routersapi.user_api import router as user_router
from digital_auto_market_fastapi.utils.security.secure_authentication import get_current_active_user


app = FastAPI(
    title="Digital Auto Market",
    description="Digital Auto Market REST API Endpoint project implemented using Fast API framework. This connect to Azure SQL Database to store & retrieve information",
    version="V0.1.0a"
)

# Include the user API router
app.include_router(user_router)

@app.get("/")
async def root(token: Annotated[str, Depends(get_current_active_user)]):
    return {"Greet": "Guten Morgen, Champ! Welcome to Digital Auto Marketplace . Your token is:", "token": token}