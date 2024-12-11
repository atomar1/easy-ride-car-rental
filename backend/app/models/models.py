from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Float, DateTime

Base = declarative_base()

# Model for ZipCode
class ZipCode(Base):
    __tablename__ = "ZipCode"
    
    ZipCode = Column(String(10), primary_key=True)
    City = Column(String(50), nullable=False)
    State = Column(String(50), nullable=False)

# Model for FuelTypes
class FuelType(Base):
    __tablename__ = "FuelTypes"
    
    FuelTypeId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Description = Column(Text)

# Model for CarTypes
class CarType(Base):
    __tablename__ = "CarTypes"
    
    CarTypeId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Description = Column(Text)

# Model for Branches
class Branch(Base):
    __tablename__ = "Branches"
    
    BranchId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    ManagerEmail = Column(String(100))
    ManagerStartDate = Column(Date)
    StreetAddress = Column(String(100))
    Apt = Column(String(20))
    ZipCode = Column(String(10), ForeignKey("ZipCode.ZipCode"))

# Model for Employees
class Employee(Base):
    __tablename__ = "Employees"
    
    Email = Column(String(100), primary_key=True)
    Password = Column(String(100), nullable=False)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Phone = Column(String(15))
    StreetAddress = Column(String(100))
    Apt = Column(String(20))
    ZipCode = Column(String(10), ForeignKey("ZipCode.ZipCode"))
    BranchId = Column(Integer, ForeignKey("Branches.BranchId"))

# Model for Cars
class Car(Base):
    __tablename__ = "Cars"
    
    CarId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100))
    Description = Column(Text)
    ModelYear = Column(Integer)
    Manufacturer = Column(String(50))
    Color = Column(String(50))
    SeatCapacity = Column(Integer)
    RegNum = Column(String(50), unique=True)
    Mileage = Column(Integer)
    DailyRate = Column(Float)
    FuelTypeId = Column(Integer, ForeignKey("CarTypes.CarTypeId"))
    CarTypeId = Column(Integer, ForeignKey("FuelTypes.FuelTypeId"))
    BranchId = Column(Integer, ForeignKey("Branches.BranchId"))

# Model for Customers
class Customer(Base):
    __tablename__ = "Customers"
    
    Email = Column(String(100), primary_key=True)
    Password = Column(String(100), nullable=False)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Phone = Column(String(15))
    StreetNumber = Column(String(100))
    Apt = Column(String(20))
    ZipCode = Column(String(10), ForeignKey("ZipCode.ZipCode"))
    DriverLicense = Column(String(50), nullable=False)

# Model for BookingStatuses
class BookingStatus(Base):
    __tablename__ = "BookingStatuses"
    
    BookingStatusId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Description = Column(Text)

# Model for Bookings
class Booking(Base):
    __tablename__ = "Bookings"
    
    BookingId = Column(Integer, primary_key=True, autoincrement=True)
    CustomerEmail = Column(String(100), ForeignKey("Customers.Email"), nullable=False)
    CarId = Column(Integer, ForeignKey("Cars.CarId"), nullable=False)
    PickUpBranchId = Column(Integer, ForeignKey("Branches.BranchId"), nullable=False)
    PickUpDate = Column(DateTime, nullable=False)
    DropOffBranchId = Column(Integer, ForeignKey("Branches.BranchId"), nullable=False)
    DropOffDate = Column(DateTime, nullable=False)
    BookingStatusId = Column(Integer, ForeignKey("BookingStatuses.BookingStatusId"), nullable=False)

# Model for RentalStatuses
class RentalStatus(Base):
    __tablename__ = "RentalStatuses"
    
    RentalStatusId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Description = Column(Text, nullable=True)

# Model for Rentings
class Renting(Base):
    __tablename__ = "Rentings"
    
    RentingId = Column(Integer, primary_key=True, autoincrement=True)
    CustomerEmail = Column(String(100), ForeignKey("Customers.Email"), nullable=False)
    CarId = Column(Integer, ForeignKey("Cars.CarId"), nullable=False)
    PickUpBranchId = Column(Integer, ForeignKey("Branches.BranchId"), nullable=False)
    EmployeeEmail = Column(String(100), ForeignKey("Employees.Email"), nullable=False)
    PickUpDate = Column(DateTime, nullable=False)
    DropOffBranchId = Column(Integer, ForeignKey("Branches.BranchId"), nullable=False)
    DropOffDate = Column(DateTime)
    Amount = Column(Float, nullable=False)
    RentalStatusId = Column(Integer, ForeignKey("RentalStatuses.RentalStatusId"), nullable=False)
