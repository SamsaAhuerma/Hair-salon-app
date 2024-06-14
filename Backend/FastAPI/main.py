from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routers import customers, appointments

app = FastAPI()

#Base de datos
customer = AsyncIOMotorClient("mongodb://localhost:27017")
database = customer["hairdresser_db"]

app.include_router(customers.router)
app.include_router(appointments.router)

#iniciar el server : uvicorn main:app --reload
@app.get("/")
async def root(): 
    return {"message": "Bienvenidas al sistema de turnos de Caotica"}



