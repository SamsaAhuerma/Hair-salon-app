from models.customer_m import Customer
from config.database import customer_collection
from schema.customer import customerEntity, customersEntity
from bson import ObjectId
from pymongo.errors import WTimeoutError, PyMongoError

class customerComunicationDB():

    def create_customer(customer: Customer):
        try:
            result = customer_collection.insert_one(dict(customer))
            customer_created = customer_collection.find_one({"_id":result.inserted_id})
            return customerEntity(customer_created)
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def get_customer_by_id(id:str):
        try:
            customer = customer_collection.find_one({"_id":ObjectId(id)})
            if customer:
                return customerEntity(customer)
            else:
                return {"error":"Customer not found!"}
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def get_list_of_customers():
        try:
            customers = customersEntity(customer_collection.find())
            return customers
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def update_customer_by_id(id:str, customer:Customer):    
        try:
            result = customer_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(customer)}, return_document=True)
            if result:
                return {"success": "Updated customer successfully"}
            else:
                return {"error": "Customer not found"}
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
    
    def delete_customer_by_id(id:str):
        try:
            result = customer_collection.find_one_and_delete({"_id":ObjectId(id)})
            if result:
                return {"success": "Deleted customer successfully"}
            else:
                return {"error": "Customer not found"}
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}