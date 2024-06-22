from fastapi import APIRouter, HTTPException, status
from typing import List
from models.servis import Servis
from db_com.servis import ServisRepository

router = APIRouter(prefix="/servis",
                    tags=["Servis"],
                    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

@router.post("/")
async def create_servis(servis: Servis):
    servis_repo = ServisRepository()

    if servis_repo.servis_exists(servis.servis_name):
        raise HTTPException(status_code=400, detail="Servis already exists")
    
    try:
        servis_repo.create_servis(servis)
        return {status.HTTP_201_CREATED: "Servis created"}
    
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error: An error occurred while creating the servis")