from fastapi import Depends, APIRouter

from digital_auto_market_fastapi.dependencies import get_db
from digital_auto_market_fastapi.routersapi import autoinfo_schema, autoinfo_crud
from digital_auto_market_fastapi.routersapi.autoinfo_schema import AutoInfoCreate
from digital_auto_market_fastapi.utils.database import models
from digital_auto_market_fastapi.utils.database.database import engine

# Refer ddl.py for in detail explanation
models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/automarket",
    tags=["Automobile Information"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)


@router.get("/all_vehicle", response_model=list[autoinfo_schema.AutoInfo])
async def get_all_autoinfo(db_session=Depends(get_db)):
    auto_list = autoinfo_crud.get_all_autoinfo(db_session)
    return auto_list

@router.post("/add_entry/vehicle", response_model=autoinfo_schema.AutoInfo)
async def create_vehicle_record( vehicle: AutoInfoCreate ,db_session=Depends(get_db)):
     return autoinfo_crud.create_vehicle_record(db_session, vehicle)


