from pydantic import BaseModel

class Appointments(BaseModel):
    servis_id: int
    customer_id: int
    servis_name: str
    servis_description: str
    servis_duration: int