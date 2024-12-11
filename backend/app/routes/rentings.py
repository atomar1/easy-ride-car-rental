from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new Renting
@router.post("/", response_model=schemas.Renting)
def create_renting(renting: schemas.RentingCreate, db: Session = Depends(get_db)):
    db_renting = models.Renting(**renting.dict())
    db.add(db_renting)
    db.commit()
    db.refresh(db_renting)
    return db_renting

# Get all Rentings
@router.get("/", response_model=List[schemas.Renting])
def get_rentings(db: Session = Depends(get_db)):
    return db.query(models.Renting).all()

# Get a single Renting by ID
@router.get("/{renting_id}", response_model=schemas.Renting)
def get_renting(renting_id: int, db: Session = Depends(get_db)):
    db_renting = db.query(models.Renting).filter(models.Renting.RentingId == renting_id).first()
    if db_renting is None:
        raise HTTPException(status_code=404, detail="Renting not found")
    return db_renting

# Update a Renting
@router.put("/{renting_id}", response_model=schemas.Renting)
def update_renting(renting_id: int, renting: schemas.RentingCreate, db: Session = Depends(get_db)):
    db_renting = db.query(models.Renting).filter(models.Renting.RentingId == renting_id).first()
    if db_renting is None:
        raise HTTPException(status_code=404, detail="Renting not found")
    
    for key, value in renting.dict().items():
        setattr(db_renting, key, value)
    
    db.commit()
    db.refresh(db_renting)
    return db_renting

# Delete a Renting
@router.delete("/{renting_id}", response_model=dict)
def delete_renting(renting_id: int, db: Session = Depends(get_db)):
    db_renting = db.query(models.Renting).filter(models.Renting.RentingId == renting_id).first()
    if db_renting is None:
        raise HTTPException(status_code=404, detail="Renting not found")
    
    db.delete(db_renting)
    db.commit()
    return {"detail": "Renting deleted successfully"}
