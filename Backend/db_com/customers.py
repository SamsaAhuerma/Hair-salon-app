from models.customer_m import Customer
from config.database import customer_collection as db
from schema.customer import customerEntity, customersEntity
from bson import ObjectId
from pymongo.errors import WTimeoutError, PyMongoError

class customerComunicationDB():

    def create_customer(customer: Customer):
        try:
            result = db.insert_one(dict(customer))
            customer_created = db.find_one({"_id":result.inserted_id})
            return customer_created
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def get_customer_by_id(id:str):
        try:
            customer = db.find_one({"_id":ObjectId(id)})
            return customer
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def get_list_of_customer():
        try:
            customers = db.find()
            return customers
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def update_customer_by_id(id:str, customer:Customer):    
        try:
            result = db.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(customer)}, return_document=True)
            return result
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def delete_customer_by_id(id:str):
        try:
            db.find_one_and_delete({"_id":ObjectId(id)})
            return {"success": "Deleted customer successfully"}
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}