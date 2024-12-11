from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()

# Create a new Employee
@router.post("/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Get all Employees
@router.get("/", response_model=List[schemas.Employee])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

# Get a single Employee by Email
@router.get("/{employee_email}", response_model=schemas.Employee)
def get_employee(employee_email: str, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.Email == employee_email).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Update an Employee
@router.put("/{employee_email}", response_model=schemas.Employee)
def update_employee(employee_email: str, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.Email == employee_email).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Delete an Employee
@router.delete("/{employee_email}", response_model=dict)
def delete_employee(employee_email: str, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.Email == employee_email).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(db_employee)
    db.commit()
    return {"detail": "Employee deleted successfully"}
