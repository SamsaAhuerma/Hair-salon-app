from fastapi import APIRouter, HTTPException, status
from typing import List
from models.appointments_m import Appointments
from schema.appointment import appointmentEntity, appointmentsEntity
from db_com.appointments import  appointmentsComunicationDB as db
from bson import ObjectId

router = APIRouter(prefix="/appointments",
                   tags=["appointments"],
                   responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Not found"}})

com_db = db()
#citas
@router.get("/", response_model=List[Appointments]) 
async def get_all_appointments():
    try: 
        return db.get_list_of_appointments()
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR0, detail="No se pudieron obtener las citas" + str(e))

@router.post("/", response_model=Appointments, status_code=201)
async def create_appointements(appointment: Appointments):
    try: 
        return db.create_appointment(appointment) 
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No se pudo crear la cita" + str(e))
    
@router.get("/{id}")
async def get_appointment(id: str):
    try:
        appointment = db.get_appointment_by_id(id) #a implementar
        if appointment is None:
            raise HTTPException(status_code=404, detail=f"No se encontró una cita con el ID: {id}")
        return appointmentEntity(appointment)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener cita. Detalle del error: " + str(e))
    
@router.put("/{id}", response_model=Appointments)
async def update_appointment(id: str, appointment_update_data: Appointments):
    try:
        update_appointment = update_appointment(id, appointment_update_data)
        if update_appointment is None:
            raise HTTPException(status_code=404, detail="No se encontró la cita con el ID: {id}")
        return update_appointment
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar cita. Detalle del error:" + str(e))
    
@router.delete("/{id}", response_model=Appointments)
async def delete_appointment(id: str):
    try:
        db.delete_appointment_by_id(id) 
        return {"message": "Cita eliminada con éxito"}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No se pudo eliminar la cita" + str(e))