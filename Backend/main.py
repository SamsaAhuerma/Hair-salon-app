from fastapi import FastAPI
from routes import appointments, customers

app = FastAPI()

app.include_router(customers.router)
app.include_router(appointments.router)

#iniciar el server : uvicorn main:app --reload
@app.get("/")
async def root(): 
    return {"message": "Bienvenidas al sistema de turnos de Caotica"}



