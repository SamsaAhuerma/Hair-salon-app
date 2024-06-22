from config.database import servis_collection

class ServisRepository:

    def create_servis(self, servis):
        servis_collection.insert_one(dict(servis))

    def servis_exists(self, servis_name):
        return servis_collection.find_one({"servis_name": servis_name})