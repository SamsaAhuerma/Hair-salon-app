from pydantic import BaseModel, Field

class Servis(BaseModel):
    servis_name: str
    servis_description: str
    servis_duration: int