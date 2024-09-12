import base64

from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from digital_auto_market_fastapi.dependencies import get_db
from digital_auto_market_fastapi.utils.database import models
from digital_auto_market_fastapi.routersapi import vdetails_schema
from digital_auto_market_fastapi.routersapi.vdetails_schema import VehicleTechSpec, VehicleDetails, VehicleDetailsCreate
from digital_auto_market_fastapi.utils.database.database import engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/vehicle_details",
    tags=["Vehicle detailed specification"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}}
)


@router.post("/add_vehicle_specs")
async def add_vehicle_specs(spec: VehicleDetailsCreate, db_session=Depends(get_db)):
    add_vehicle_specs_by_name(spec, db_session)
    return "New vehicle specification added into DB successfully"


@router.get("/get_vehicle_specs/{vehicle_id}", response_model=VehicleDetails)
async def get_vehicle_specs(vehicle_id, db_session=Depends(get_db)):
    vehicle_spec = get_vehicle_specs_by_id(vehicle_id, db_session)
    if vehicle_spec is None:
        return False
    return vehicle_spec


def add_vehicle_specs_by_name(spec: VehicleDetailsCreate, db_session: Session):
    print(f"before converting to model: {spec.photo}")
    if spec.photo:
        photo_data = base64.b64decode(spec.photo)
    else:
        photo_data = None

    print(f"after converting to base64: {spec.photo}")
    # Prepare the new vehicle specification model
    new_vehicle_spec = models.VehicleDetails(

        photo=photo_data,  # Set binary data here
        history=spec.history
    )
    db_session.add(new_vehicle_spec)
    db_session.commit()
    db_session.refresh(new_vehicle_spec)
    return new_vehicle_spec


def get_vehicle_specs_by_id(vehicle_id: str, db_session: Session):
    # Fetch the vehicle details by vehicle_id
    vehicle_spec = db_session.query(models.VehicleDetails).filter(models.VehicleDetails.id == vehicle_id).first()

    if not vehicle_spec:
        return None
        # Assuming `vehicle_spec.photo` is in bytes, encode it to base64
    if vehicle_spec.photo:
        vehicle_spec.photo = base64.b64encode(vehicle_spec.photo).decode('utf-8')
    return vehicle_spec
