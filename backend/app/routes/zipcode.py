from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new ZipCode
@router.post("/", response_model=schemas.ZipCode)
def create_zipcode(zipcode: schemas.ZipCodeCreate, db: Session = Depends(get_db)):
    db_zipcode = models.ZipCode(**zipcode.dict())
    db.add(db_zipcode)
    db.commit()
    db.refresh(db_zipcode)
    return db_zipcode

# Get all ZipCodes
@router.get("/", response_model=List[schemas.ZipCode])
def get_zipcodes(db: Session = Depends(get_db)):
    return db.query(models.ZipCode).all()

# Get a single ZipCode by code
@router.get("/{zipcode}", response_model=schemas.ZipCode)
def get_zipcode(zipcode: str, db: Session = Depends(get_db)):
    db_zipcode = db.query(models.ZipCode).filter(models.ZipCode.ZipCode == zipcode).first()
    if db_zipcode is None:
        raise HTTPException(status_code=404, detail="ZipCode not found")
    return db_zipcode

# Update a ZipCode
@router.put("/{zipcode}", response_model=schemas.ZipCode)
def update_zipcode(zipcode: str, zipcode_data: schemas.ZipCodeCreate, db: Session = Depends(get_db)):
    db_zipcode = db.query(models.ZipCode).filter(models.ZipCode.ZipCode == zipcode).first()
    if db_zipcode is None:
        raise HTTPException(status_code=404, detail="ZipCode not found")
    
    for key, value in zipcode_data.dict().items():
        setattr(db_zipcode, key, value)
    
    db.commit()
    db.refresh(db_zipcode)
    return db_zipcode

# Delete a ZipCode
@router.delete("/{zipcode}", response_model=dict)
def delete_zipcode(zipcode: str, db: Session = Depends(get_db)):
    db_zipcode = db.query(models.ZipCode).filter(models.ZipCode.ZipCode == zipcode).first()
    if db_zipcode is None:
        raise HTTPException(status_code=404, detail="ZipCode not found")
    
    db.delete(db_zipcode)
    db.commit()
    return {"detail": "ZipCode deleted successfully"}
