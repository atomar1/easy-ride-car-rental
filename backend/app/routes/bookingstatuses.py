from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new BookingStatus
@router.post("/", response_model=schemas.BookingStatus)
def create_bookingstatus(bookingstatus: schemas.BookingStatusCreate, db: Session = Depends(get_db)):
    db_bookingstatus = models.BookingStatus(**bookingstatus.dict())
    db.add(db_bookingstatus)
    db.commit()
    db.refresh(db_bookingstatus)
    return db_bookingstatus

# Get all BookingStatuses
@router.get("/", response_model=List[schemas.BookingStatus])
def get_bookingstatuses(db: Session = Depends(get_db)):
    return db.query(models.BookingStatus).all()

# Get a single BookingStatus by ID
@router.get("/{bookingstatus_id}", response_model=schemas.BookingStatus)
def get_bookingstatus(bookingstatus_id: int, db: Session = Depends(get_db)):
    db_bookingstatus = db.query(models.BookingStatus).filter(models.BookingStatus.BookingStatusId == bookingstatus_id).first()
    if db_bookingstatus is None:
        raise HTTPException(status_code=404, detail="BookingStatus not found")
    return db_bookingstatus

# Update a BookingStatus
@router.put("/{bookingstatus_id}", response_model=schemas.BookingStatus)
def update_bookingstatus(bookingstatus_id: int, bookingstatus: schemas.BookingStatusCreate, db: Session = Depends(get_db)):
    db_bookingstatus = db.query(models.BookingStatus).filter(models.BookingStatus.BookingStatusId == bookingstatus_id).first()
    if db_bookingstatus is None:
        raise HTTPException(status_code=404, detail="BookingStatus not found")
    
    for key, value in bookingstatus.dict().items():
        setattr(db_bookingstatus, key, value)
    
    db.commit()
    db.refresh(db_bookingstatus)
    return db_bookingstatus

# Delete a BookingStatus
@router.delete("/{bookingstatus_id}", response_model=dict)
def delete_bookingstatus(bookingstatus_id: int, db: Session = Depends(get_db)):
    db_bookingstatus = db.query(models.BookingStatus).filter(models.BookingStatus.BookingStatusId == bookingstatus_id).first()
    if db_bookingstatus is None:
        raise HTTPException(status_code=404, detail="BookingStatus not found")
    
    db.delete(db_bookingstatus)
    db.commit()
    return {"detail": "BookingStatus deleted successfully"}
