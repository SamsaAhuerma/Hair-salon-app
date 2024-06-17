from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List

#customers /clientes
#iniciar el server : uvicorn customers:app --reload
router = APIRouter()

def get_database() -> AsyncIOMotorDatabase:
    from main import database
    return database
@router.get("/customers", response_model=List[dict]) 
async def read_customer():
    return [{"id": 1, "client": "John Doe"}]

