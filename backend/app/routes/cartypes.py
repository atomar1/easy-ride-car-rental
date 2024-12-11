from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new CarType
@router.post("/", response_model=schemas.CarType)
def create_cartype(cartype: schemas.CarTypeCreate, db: Session = Depends(get_db)):
    db_cartype = models.CarType(**cartype.dict())
    db.add(db_cartype)
    db.commit()
    db.refresh(db_cartype)
    return db_cartype

# Get all CarTypes
@router.get("/", response_model=List[schemas.CarType])
def get_cartypes(db: Session = Depends(get_db)):
    return db.query(models.CarType).all()

# Get a single CarType by ID
@router.get("/{cartype_id}", response_model=schemas.CarType)
def get_cartype(cartype_id: int, db: Session = Depends(get_db)):
    db_cartype = db.query(models.CarType).filter(models.CarType.CarTypeId == cartype_id).first()
    if db_cartype is None:
        raise HTTPException(status_code=404, detail="CarType not found")
    return db_cartype

# Update a CarType
@router.put("/{cartype_id}", response_model=schemas.CarType)
def update_cartype(cartype_id: int, cartype: schemas.CarTypeCreate, db: Session = Depends(get_db)):
    db_cartype = db.query(models.CarType).filter(models.CarType.CarTypeId == cartype_id).first()
    if db_cartype is None:
        raise HTTPException(status_code=404, detail="CarType not found")
    
    for key, value in cartype.dict().items():
        setattr(db_cartype, key, value)
    
    db.commit()
    db.refresh(db_cartype)
    return db_cartype

# Delete a CarType
@router.delete("/{cartype_id}", response_model=dict)
def delete_cartype(cartype_id: int, db: Session = Depends(get_db)):
    db_cartype = db.query(models.CarType).filter(models.CarType.CarTypeId == cartype_id).first()
    if db_cartype is None:
        raise HTTPException(status_code=404, detail="CarType not found")
    
    db.delete(db_cartype)
    db.commit()
    return {"detail": "CarType deleted successfully"}
