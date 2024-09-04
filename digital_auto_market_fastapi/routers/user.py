from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "wade"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return [{"username": "fakecurrentuser"}]