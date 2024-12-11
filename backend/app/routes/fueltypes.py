from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new FuelType
@router.post("/", response_model=schemas.FuelType)
def create_fueltype(fueltype: schemas.FuelTypeCreate, db: Session = Depends(get_db)):
    db_fueltype = models.FuelType(**fueltype.dict())
    db.add(db_fueltype)
    db.commit()
    db.refresh(db_fueltype)
    return db_fueltype

# Get all FuelTypes
@router.get("/", response_model=List[schemas.FuelType])
def get_fueltypes(db: Session = Depends(get_db)):
    return db.query(models.FuelType).all()

# Get a single FuelType by ID
@router.get("/{fueltype_id}", response_model=schemas.FuelType)
def get_fueltype(fueltype_id: int, db: Session = Depends(get_db)):
    db_fueltype = db.query(models.FuelType).filter(models.FuelType.FuelTypeId == fueltype_id).first()
    if db_fueltype is None:
        raise HTTPException(status_code=404, detail="FuelType not found")
    return db_fueltype

# Update a FuelType
@router.put("/{fueltype_id}", response_model=schemas.FuelType)
def update_fueltype(fueltype_id: int, fueltype: schemas.FuelTypeCreate, db: Session = Depends(get_db)):
    db_fueltype = db.query(models.FuelType).filter(models.FuelType.FuelTypeId == fueltype_id).first()
    if db_fueltype is None:
        raise HTTPException(status_code=404, detail="FuelType not found")
    
    for key, value in fueltype.dict().items():
        setattr(db_fueltype, key, value)
    
    db.commit()
    db.refresh(db_fueltype)
    return db_fueltype

# Delete a FuelType
@router.delete("/{fueltype_id}", response_model=dict)
def delete_fueltype(fueltype_id: int, db: Session = Depends(get_db)):
    db_fueltype = db.query(models.FuelType).filter(models.FuelType.FuelTypeId == fueltype_id).first()
    if db_fueltype is None:
        raise HTTPException(status_code=404, detail="FuelType not found")
    
    db.delete(db_fueltype)
    db.commit()
    return {"detail": "FuelType deleted successfully"}
