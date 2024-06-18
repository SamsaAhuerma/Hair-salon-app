from pydantic import BaseModel
from typing import List
from appointments_m import Appointments

class Customer(BaseModel):
    name: str
    email: str
    phone: str
    appointments: List[Appointments] = []
