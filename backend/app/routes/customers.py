from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new Customer
@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Get all Customers
@router.get("/", response_model=List[schemas.Customer])
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

# Get a single Customer by Email
@router.get("/{customer_email}", response_model=schemas.Customer)
def get_customer(customer_email: str, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.Email == customer_email).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# Update a Customer
@router.put("/{customer_email}", response_model=schemas.Customer)
def update_customer(customer_email: str, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.Email == customer_email).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    for key, value in customer.dict().items():
        setattr(db_customer, key, value)
    
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Delete a Customer
@router.delete("/{customer_email}", response_model=dict)
def delete_customer(customer_email: str, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.Email == customer_email).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db.delete(db_customer)
    db.commit()
    return {"detail": "Customer deleted successfully"}
