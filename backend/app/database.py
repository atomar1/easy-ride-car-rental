from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.models import Base 
from app.config import settings

# MySQL database credentials
DATABASE_URL = "mysql+mysqlconnector://root:workingwithdatabase%400606@localhost:3306/easy_ride_car_rental"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()