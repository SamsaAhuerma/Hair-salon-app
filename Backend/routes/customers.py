from fastapi import APIRouter, HTTPException, status
from typing import List
from models.customer_m import Customer
from db_com.customers import customerComunicationDB
from schema.customer import customerEntity, customersEntity

#customers /clientes
#iniciar el server : uvicorn customers:app --reload
router = APIRouter()

@router.get("/customers", response_model=List[dict]) 
async def get_all_customer():
    try:
        customers = customerComunicationDB.get_list_of_customer()
        return customersEntity(customers)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")

@router.post("/customers")
async def create_customer(customer : Customer):
    #falta validación de datos acá ?¿
    try:
        customer_created = customerComunicationDB.create_customer(customer)
        return customerEntity(customer_created)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")
    
    
@router.get("/customers/{id}")
async def get_customer(id:str):
    try:
        customer = customerComunicationDB.get_customer_by_id(id)
        if not customer:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Customer not found")
        return customerEntity(customer)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")

@router.put("/customers/{id}")
async def update_customer(id:str, customer:Customer):
    try:
        result =customerComunicationDB.update_customer_by_id(id, customer)
        if not result:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Customer not found")
        return {"success": "Updated customer successfully"} 
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")
    
@router.delete("/customers/{id}")
async def delete_customer(id:str):
    try: 
        if not customerComunicationDB.get_customer_by_id(id):
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Customer not found")
        return customerComunicationDB.delete_customer_by_id(id)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")