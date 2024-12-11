from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .models import Branch
from .models import Car
from .models import CarType
from .models import Customer
from .models import Employee
from .models import FuelType
from .models import Booking
from .models import BookingStatus
from .models import Renting
from .models import RentalStatus
from .models import ZipCode