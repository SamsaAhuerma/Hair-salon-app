from pydantic import BaseModel, Field
from datetime import datetime 

class Appointments(BaseModel):
    time: datetime= Field(...,description="Scheduled time for the appointment")
    date : datetime= Field(...,description="Date of apointment") 
    message : str= Field(...,description="Message of confirmation or notes for the appointment")