from pydantic import BaseModel

class Servis(BaseModel):
    servis_name: str
    servis_description: str
    servis_duration: int