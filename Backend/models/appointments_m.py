from pydantic import BaseModel

class Appointments(BaseModel):
    customer_id: str
    time: str