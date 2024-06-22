from models.appointments_m import Appointments
from config.database import appointment_collection
from schema.appointment import appointmentEntity, appointmentsEntity
from bson import ObjectId

class appointmentsComunicationDB():

    def create_appointment(appointment: Appointments):
        result = appointment_collection.insert_one(dict(appointment))
        appointment_created = appointment_collection.find_one({"_id": result.inserted_id})
        return appointment_created
    
    def get_appointment_by_id(id: str):
        appointment = appointment_collection.find_one({"_id": ObjectId(id)})
        return appointment
    
    def get_all_appointments():
        appointment = appointmentsEntity(appointment_collection.find())
        return appointment
    
    def update_appointment_by_id(id: str, appointment: Appointments):
        result = appointment_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": dict(appointment)},
            return_document=True
        )    
        return {"success": "Updated appointment successfully"}

    def delete_appointment_by_id(id: str):
        result = appointment_collection.find_one_and_delete({"_id": ObjectId(id)})
        return {"success": "Deleted appointment successfully"}
        