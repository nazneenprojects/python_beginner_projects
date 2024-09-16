from beanie import Document

from pydantic import BaseModel, EmailStr


class User(Document):
    email: EmailStr
    password: str

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "jennmerkel@kdp.com",
                "password": "ChangeMe!!!"
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str