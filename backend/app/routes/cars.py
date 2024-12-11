from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new Car
@router.post("/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# Get all Cars
@router.get("/", response_model=List[schemas.Car])
def get_cars(db: Session = Depends(get_db)):
    return db.query(models.Car).all()

# Get a single Car by ID
@router.get("/{car_id}", response_model=schemas.Car)
def get_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(models.Car).filter(models.Car.CarId == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

# Update a Car
@router.put("/{car_id}", response_model=schemas.Car)
def update_car(car_id: int, car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = db.query(models.Car).filter(models.Car.CarId == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    
    for key, value in car.dict().items():
        setattr(db_car, key, value)
    
    db.commit()
    db.refresh(db_car)
    return db_car

# Delete a Car
@router.delete("/{car_id}", response_model=dict)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(models.Car).filter(models.Car.CarId == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    
    db.delete(db_car)
    db.commit()
    return {"detail": "Car deleted successfully"}
