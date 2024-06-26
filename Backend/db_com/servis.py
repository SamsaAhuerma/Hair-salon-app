from config.database import servis_collection as db
from pymongo.errors import DuplicateKeyError ,WTimeoutError, PyMongoError

class ServisComunicationDB():

    def create_servis(self, servis):
        try:
            db.insert_one(dict(servis))
        except DuplicateKeyError:
            raise Exception("Servis already exists")
        except WTimeoutError:
            raise Exception("Timeout expired querying the database")
        except PyMongoError as e:
            raise Exception(f"An error occurred while getting the servis list {e}")

    def exists_servis_by_name(self, servis_name):
        try:
            return db.find_one({"servis_name": servis_name})
        except WTimeoutError:
            raise Exception("Timeout expired querying the database")
        except PyMongoError as e:
            raise Exception(f"An error occurred while getting the servis list {e}")
    
    def get_list_of_servis(self):
        try:
            return db.find()
        except WTimeoutError:
            raise Exception("Timeout expired querying the database")
        except PyMongoError as e:
            raise Exception(f"An error occurred while getting the servis list {e}")

    def get_servis_by_id(self, servis_id):
        try:
            return db.find_one({"_id": servis_id})
        except WTimeoutError:
            raise Exception("Timeout expired querying the database")
        except PyMongoError as e:
            raise Exception(f"An error occurred while getting the servis list {e}")
    
    def update_servis_by_id(self, servis_id, servis):
        try:
            return db.find_one_and_update({"_id": servis_id}, {"$set": dict(servis)})
        except WTimeoutError:
            raise Exception("Timeout expired querying the database")
        except PyMongoError as e:
            raise Exception(f"An error occurred while getting the servis list {e}")

    def delete_servis_by_id(self, servis_id):
        try:
            return db.find_one_and_delete({"_id": servis_id})
        except WTimeoutError:
            raise Exception("Timeout expired querying the database")
        except PyMongoError as e:
            raise Exception(f"An error occurred while getting the servis list {e}")
        