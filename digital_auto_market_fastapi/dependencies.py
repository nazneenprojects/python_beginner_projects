from digital_auto_market_fastapi.utils.database.database import SessionLocal


# Dependency of Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()