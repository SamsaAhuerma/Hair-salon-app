from fastapi import APIRouter
from typing import List
from models.customer_m import Customer
from config.database import customer_collection
from schema.customer import customerEntity, customersEntity
from bson import ObjectId

#customers /clientes
#iniciar el server : uvicorn customers:app --reload
router = APIRouter()

@router.get("/customers", response_model=List[dict]) 
async def get_all_customers():
    customers = customersEntity(customer_collection.find())
    return customers

@router.post("/customers")
async def create_customer(customer : Customer):
    customer_collection.insert_one(dict(customer))

@router.get("/customers/{id}")
async def get_customer(id:str):
    customer = customer_collection.find_one({"_id":ObjectId(id)})
    return customerEntity(customer)

@router.put("/customers/{id}")
async def update_customer(id:str, customer:Customer):
    customer_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(customer)})

@router.delete("/customers/{id}")
async def delete_customer(id:str):
    customer_collection.find_one_and_delete({"_id":ObjectId(id)})