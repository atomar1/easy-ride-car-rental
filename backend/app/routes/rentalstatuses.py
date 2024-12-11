from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new RentalStatus
@router.post("/", response_model=schemas.RentalStatus)
def create_rental(rental: schemas.RentalStatusCreate, db: Session = Depends(get_db)):
    db_rental = models.RentalStatus(**rental.dict())
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

# Get all RentalStatuses
@router.get("/", response_model=List[schemas.RentalStatus])
def get_rentals(db: Session = Depends(get_db)):
    return db.query(models.RentalStatus).all()

# Get a single RentalStatus by ID
@router.get("/{rental_id}", response_model=schemas.RentalStatus)
def get_rental(rental_id: int, db: Session = Depends(get_db)):
    db_rental = db.query(models.RentalStatus).filter(models.RentalStatus.RentalStatusId == rental_id).first()
    if db_rental is None:
        raise HTTPException(status_code=404, detail="RentalStatus not found")
    return db_rental

# Update a RentalStatus
@router.put("/{rental_id}", response_model=schemas.RentalStatus)
def update_rental(rental_id: int, rental: schemas.RentalStatusCreate, db: Session = Depends(get_db)):
    db_rental = db.query(models.RentalStatus).filter(models.RentalStatus.RentalStatusId == rental_id).first()
    if db_rental is None:
        raise HTTPException(status_code=404, detail="RentalStatus not found")
    
    for key, value in rental.dict().items():
        setattr(db_rental, key, value)
    
    db.commit()
    db.refresh(db_rental)
    return db_rental

# Delete a RentalStatus
@router.delete("/{rental_id}", response_model=dict)
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    db_rental = db.query(models.RentalStatus).filter(models.RentalStatus.RentalStatusId == rental_id).first()
    if db_rental is None:
        raise HTTPException(status_code=404, detail="RentalStatus not found")
    
    db.delete(db_rental)
    db.commit()
    return {"detail": "RentalStatus deleted successfully"}
