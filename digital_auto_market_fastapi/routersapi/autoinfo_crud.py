from sqlalchemy.orm import Session
from digital_auto_market_fastapi.routersapi import autoinfo_schema
from digital_auto_market_fastapi.utils.database import models


def get_all_autoinfo(db_session: Session):
    return db_session.query(models.AutoInfo).all()


def get_autoinfo_byyear(db_session: Session, year: str):
    return db_session.query(models.AutoInfo).filter(models.AutoInfo.year == year)


def get_autoinfo_bybrand(db_session: Session, brand: str):
    return db_session.query(models.AutoInfo).filter_by(brand)


def create_vehicle_record(db_session: Session, vehicle: autoinfo_schema.AutoInfoCreate):
    new_vehicle = models.AutoInfo(**vehicle.dict())
    db_session.add(new_vehicle)
    db_session.add(new_vehicle)
    db_session.commit()
    db_session.refresh(new_vehicle)
    return new_vehicle


def update_vehicle_record(db_session: Session, vehicle_name: str, vehicle_count: int):
    update_vehicle = db_session.query(models.AutoInfo).filter(models.AutoInfo.vehicle_name == vehicle_name).first()

    if update_vehicle:
        update_vehicle.count = vehicle_count
        db_session.commit()
        db_session.refresh(update_vehicle)
        return update_vehicle
    return f"Successfully updated vehicle info for {vehicle_name}"


def delete_vehicle_record(db_session: Session, vehicle_name: str):
    delete_vehicle = db_session.query(models.AutoInfo).filter(models.AutoInfo.vehicle_name == vehicle_name).first()

    if delete_vehicle:
        db_session.delete(delete_vehicle)
        return True
    return f"Successfully deleted {vehicle_name} from database"
