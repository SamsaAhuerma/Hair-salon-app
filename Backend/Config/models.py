from pydantic import BaseModel
from typing import List

class Appointments(BaseModel):
    id: int
    customer_id: str
    time: str

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    appointments: List[Appointments] = []


