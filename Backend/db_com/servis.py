from config.database import servis_collection
from pymongo import errors

class ServisRepository:

    def create_servis(self, servis):
        try:
            servis_collection.insert_one(dict(servis))
        except errors.DuplicateKeyError:
            raise Exception("Servis already exists")

    def servis_exists(self, servis_name):
        return servis_collection.find_one({"servis_name": servis_name})
    
    def get_all_servis(self):
        return servis_collection.find()
    
    def get_servis_by_id(self, servis_id):
        return servis_collection.find_one({"_id": servis_id})
    
    def update_servis(self, servis_id, servis):
        servis_collection.find_one_and_update({"_id": servis_id}, {"$set": dict(servis)})

    def delete_servis(self, servis_id):
        servis_collection.find_one_and_delete({"_id": servis_id})