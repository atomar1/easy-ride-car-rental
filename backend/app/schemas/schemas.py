from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# ZipCode Schema
class ZipCodeBase(BaseModel):
    ZipCode: str
    City: str
    State: str

class ZipCodeCreate(ZipCodeBase):
    pass

class ZipCode(ZipCodeBase):
    class Config:
        orm_mode = True

# FuelTypes Schema
class FuelTypeBase(BaseModel):
    Name: str
    Description: Optional[str]

class FuelTypeCreate(FuelTypeBase):
    pass

class FuelType(FuelTypeBase):
    FuelTypeId: int

    class Config:
        orm_mode = True

# CarTypes Schema
class CarTypeBase(BaseModel):
    Name: str
    Description: Optional[str]

class CarTypeCreate(CarTypeBase):
    pass

class CarType(CarTypeBase):
    CarTypeId: int

    class Config:
        orm_mode = True

# Branches Schema
class BranchBase(BaseModel):
    Name: str
    ManagerEmail: Optional[str]
    ManagerStartDate: Optional[date]
    StreetAddress: Optional[str]
    Apt: Optional[str]
    ZipCode: str

class BranchCreate(BranchBase):
    pass

class Branch(BranchBase):
    BranchId: int

    class Config:
        orm_mode = True

# Employees Schema
class EmployeeBase(BaseModel):
    Email: str
    Password: str
    FirstName: str
    LastName: str
    Phone: Optional[str]
    StreetAddress: Optional[str]
    Apt: Optional[str]
    ZipCode: str
    BranchId: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    class Config:
        orm_mode = True

# Cars Schema
class CarBase(BaseModel):
    Name: str
    Description: Optional[str]
    BranchId: int
    Manufacturer: str
    Mileage: int
    ModelYear: int
    Color: str
    RegNum: str
    SeatCapacity: int
    DailyRate: float
    FuelTypeId: int
    CarTypeId: int

class CarCreate(CarBase):
    pass

class Car(CarBase):
    CarId: int

    class Config:
        orm_mode = True

# Customers Schema
class CustomerBase(BaseModel):
    Email: str
    Password: str
    DriverLicense: str
    FirstName: str
    LastName: str
    Phone: Optional[str]
    StreetNumber: Optional[str]
    Apt: Optional[str]
    ZipCode: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    class Config:
        orm_mode = True

# BookingStatuses Schema
class BookingStatusBase(BaseModel):
    Name: str
    Description: Optional[str]

class BookingStatusCreate(BookingStatusBase):
    pass

class BookingStatus(BookingStatusBase):
    BookingStatusId: int

    class Config:
        orm_mode = True

# Bookings Schema
class BookingBase(BaseModel):
    CustomerEmail: str
    PickUpBranchId: int
    PickUpDate: date
    DropOffBranchId: int
    DropOffDate: date
    CarId: int
    BookingStatusId: int

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    BookingId: int

    class Config:
        orm_mode = True

# RentalStatuses Schema
class RentalStatusBase(BaseModel):
    Name: str
    Description: Optional[str]

class RentalStatusCreate(RentalStatusBase):
    pass

class RentalStatus(RentalStatusBase):
    RentalStatusId: int

    class Config:
        orm_mode = True

# Rentings Schema
class RentingBase(BaseModel):
    CustomerEmail: str
    PickUpBranchId: int
    PickUpDate: date
    DropOffBranchId: int
    DropOffDate: date
    EmployeeEmail: str
    CarId: int
    Amount: float
    RentalStatusId: int

class RentingCreate(RentingBase):
    pass

class Renting(RentingBase):
    RentingId: int

    class Config:
        orm_mode = True
