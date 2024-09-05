from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm

from digital_auto_market_fastapi.routersapi.user_response_model import User
from digital_auto_market_fastapi.utils.database.database_connect import SessionLocal
from digital_auto_market_fastapi.utils.security.secure_authentication import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token, get_current_active_user

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    db_session = SessionLocal()
    user = authenticate_user(db_session, form_data.username, form_data.password)
    db_session.close()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.get("/users/activeuser/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

@router.get("/users/profile/purchaselist/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Mercedes Benz 220SE Ponton Coupe 1960", "owner": current_user.username}]
