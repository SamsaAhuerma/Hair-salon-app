from fastapi import APIRouter
from typing import List
from models.customer_m import Customer
from db_com.customers import customerComunicationDB

#customers /clientes
#iniciar el server : uvicorn customers:app --reload
router = APIRouter()

@router.get("/customers", response_model=List[dict]) 
async def get_all_customers():
    return customerComunicationDB.get_list_of_customers()

@router.post("/customers")
async def create_customer(customer : Customer):
    #falta validación de datos acá ?¿
    return customerComunicationDB.create_customer(customer)

@router.get("/customers/{id}")
async def get_customer(id:str):
    return customerComunicationDB.get_customer_by_id(id)

@router.put("/customers/{id}")
async def update_customer(id:str, customer:Customer):
    #falta validación de datos acá ?¿
    return customerComunicationDB.update_customer_by_id(id, customer)

@router.delete("/customers/{id}")
async def delete_customer(id:str):
    return customerComunicationDB.delete_customer_by_id(id)