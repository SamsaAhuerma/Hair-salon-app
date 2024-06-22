from fastapi import APIRouter, HTTPException, status
from typing import List
from models.servis import Servis
from db_com.servis import ServisRepository
from schema.servis import servisEntity, servicesEntity
from bson import ObjectId


router = APIRouter(prefix="/servis",
                    tags=["Servis"],
                    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

servis_repo = ServisRepository()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_servis(servis: Servis):
    if servis_repo.exists_servis_by_name(servis.servis_name):
        raise HTTPException(status_code=400, detail="Servis already exists")
    
    try:
        servis_repo.create_servis(servis)
        return {"Servis created successfully"}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {e}")
    

@router.get("/", response_model=List[dict])
async def get_all_servis():
    try:
        services = servis_repo.get_all_servis()
        return servicesEntity(services)
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {e}")
    

@router.get("/{id}", response_model=dict)
async def get_servis(id: str):
    try:
        servis = servis_repo.get_servis_by_id(ObjectId(id))
        if servis:
            return servisEntity(servis)
        else:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Servis not found")
    except Exception as e:
        raise e if isinstance(e, HTTPException) else HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Internal server error: {e}")
    

@router.put("/{id}")
async def update_servis(id: str, servis: Servis):
    if not servis_repo.get_servis_by_id(ObjectId(id)):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Servis not found")
    try:
        servis_repo.update_servis(ObjectId(id), servis)
        return {"Servis updated successfully"}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {e}")
    

@router.delete("/{id}")
async def delete_servis(id: str):
    if not servis_repo.get_servis_by_id(ObjectId(id)):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Servis not found")
    try:
        servis_repo.delete_servis(ObjectId(id))
        return {"Servis deleted successfully"}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal server error: {e}")