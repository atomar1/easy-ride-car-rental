from fastapi import FastAPI
from app.routes import bookings, rentings, branches, employees, cars, customers, fueltypes, cartypes, bookingstatuses, rentalstatuses, zipcode

app = FastAPI()

# the routes
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
app.include_router(rentings.router, prefix="/rentings", tags=["Rentings"])
app.include_router(branches.router, prefix="/branches", tags=["Branches"])
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(cars.router, prefix="/cars", tags=["Cars"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(fueltypes.router, prefix="/fuel-types", tags=["FuelTypes"])
app.include_router(cartypes.router, prefix="/car-types", tags=["CarTypes"])
app.include_router(bookingstatuses.router, prefix="/booking-statuses", tags=["BookingStatuses"])
app.include_router(rentalstatuses.router, prefix="/rental-statuses", tags=["RentalStatuses"])
app.include_router(zipcode.router, prefix="/zip-codes", tags=["ZipCodes"])