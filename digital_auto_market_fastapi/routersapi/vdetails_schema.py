import base64
from traceback import print_tb

from pydantic import BaseModel, Field
from typing import Optional, List, TYPE_CHECKING


class VehicleTechSpec(BaseModel):
    engine_speed: float = Field(..., example=0.0)
    torque: float = Field(..., example=660.0)
    max_load: float = Field(..., example=500.0)


class VehicleDetailsBase(BaseModel):
    photo: Optional[bytes] = Field(None, example="0x1234567890ABCDEF")  # Binary data for photo
    history: Optional[str] = Field(None, example="""{{
    "name": "Volvo XZ400",
    "manufactured": "2020",
    "sound_level": "low",
    "emission": "zero",
    "Tech_spec": {
        "engine_speed": 400.0,’
        "torque": 450.0,
        "max_load": 1000.0
    }
}""")  # JSON history as a string

    class Config:
        orm_mode = True  # Required to work with SQLAlchemy models

    def __init__(self, **data):
        super().__init__(**data)
        if self.photo:
            self.photo = base64.b64encode(self.photo).decode('utf-8')  # Encode binary to base64 string


class VehicleDetails(VehicleDetailsBase):
    id: int

    # Define relationship with AutoInfo
    # auto_infos: List["AutoInfo"] = []  # List of related AutoInfoE

    class Config:
        orm_mode = True


class VehicleDetailsCreate(VehicleDetailsBase):
    pass


class VehicleDetailsUpdate(BaseModel):
    photo: Optional[str] = None
    history: Optional[str] = None

    class Config:
        orm_mode = True
