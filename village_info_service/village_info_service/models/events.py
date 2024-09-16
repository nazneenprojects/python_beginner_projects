from typing import Optional, List

from beanie import Document
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Yoga Club Session",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be teaching and learning yoga together in early morning with sunshine. Come & join to find peace together!",
                "tags": ["yoga", "all-gender", "morning", "health"],
                "location": "Central Park"
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Yoga Club Session",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be teaching and learning yoga together in early morning with sunshine. Come & join to find peace together!",
                "tags": ["yoga", "all-gender", "morning", "health"],
                "location": "Central Park"
            }
        }