from models.appointments_m import Appointments
from config.database import appointment_collection as db 
from schema.appointment import appointmentEntity, appointmentsEntity
from pymongo.errors import DuplicateKeyError ,WTimeoutError, PyMongoError
from bson import ObjectId

class appointmentsComunicationDB():

    def create_appointment(appointment: Appointments):
        try:
            db.insert_one(dict(appointment))
            appointment_created = db.find_one({"_id": db.inserted_id})
            return appointment_created
        except WTimeoutError:
            return {"error": "TimeoutError"}
        except PyMongoError as e:
            return {"error": str(e)}
        
    def get_appointment_by_id(id: str):
        try:
            return db.find_one({"_id": ObjectId(id)})
        except WTimeoutError:
            return {"error": "TimeoutError"}
        except PyMongoError as e:
            return {"error": str(e)}
    
    def get_list_of_appointments():
        try:
            return appointmentsEntity(db.find())
        except WTimeoutError:
            return {"error": "TimeoutError"}
        except PyMongoError as e:
            return {"error": str(e)}
        
    def update_appointment_by_id(id: str, appointment: Appointments):
        try:
            return db.find_one_and_update(
                {"_id": ObjectId(id)}, {"$set": dict(appointment)}, return_document=True)    
        except WTimeoutError:
            return {"error": "TimeoutError"}
        except PyMongoError as e:
            return {"error": str(e)}
        
    def delete_appointment_by_id(id: str):
       try:
           return db.find_one_and_delete({"_id": ObjectId(id)})
       except WTimeoutError:
           return {"error": "TimeoutError"}
       except PyMongoError as e:
           return {"error": str(e)}