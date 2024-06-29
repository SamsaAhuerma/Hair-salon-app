from pydantic import BaseModel, EmailStr
from typing import List
from models.appointments_m import Appointments

class Customer(BaseModel):
    name: str
    email: EmailStr
    phone: str
    appointments: List[Appointments] = []
