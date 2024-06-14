from fastapi import APIRouter

router = APIRouter()


#citas
@router.get("/appointments") 
async def read_appointments():
    return [{"id": 1, "client": "John Doe"}]
