from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint, Numeric, VARBINARY, NVARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from digital_auto_market_fastapi.utils.database.database import Base


class UserInDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    full_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    disabled = Column(Boolean, default=False)

class VehicleDetails(Base):
    __tablename__ = "v_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(VARBINARY, nullable=True)
    history = Column(NVARCHAR, nullable=True)

    # Define relationship with AutoInfo
    auto_infos = relationship("AutoInfo", back_populates="vehicle_details",  cascade="all, delete-orphan")

class AutoInfo(Base):
    __tablename__ = "auto_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_name = Column(String(255), nullable=False)          # Vehicle name as string
    vehicle_model = Column(String(255), nullable=False)         # Vehicle model as string
    num_wheel = Column(Integer, nullable=False)                 # Number of wheels as an integer
    type = Column(String(50), CheckConstraint("type IN ('ev', 'non-ev')"), nullable=False)  # Type either 'ev' or 'non-ev'
    year = Column(Integer, CheckConstraint("year >= 1886"), nullable=False)  # Year with constraint (1886 onward)
    brand = Column(String(255), nullable=False)                 # Brand as string
    price = Column(Numeric(18, 2), nullable=False)  # Price as decimal with 2 precision points for euros
    available = Column(Boolean, default=True)                   # Available flag, default set to true (1)
    reserved = Column(Boolean, default=False)                   # Reserved flag, default set to false (0)
    count = Column(Integer, default=0)                          # Count of available vehicles
    v_id = Column(Integer, ForeignKey('v_details.id'), nullable=False)

    # Additional constraints
    __table_args__ = (
        CheckConstraint("type IN ('ev', 'non-ev')", name="check_vehicle_type"),
        CheckConstraint("year >= 1886", name="check_vehicle_year"),
    )

    # Define relationship with VehicleDetails
    vehicle_details = relationship("VehicleDetails", back_populates="auto_infos")



