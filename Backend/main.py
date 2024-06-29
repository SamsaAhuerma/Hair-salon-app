from fastapi import FastAPI
from routes import appointments, customers, servis

app = FastAPI()

app.include_router(customers.router)
app.include_router(appointments.router)
app.include_router(servis.router)

#iniciar el server : uvicorn main:app --reload
@app.get("/")
async def root(): 
    return {"message": "Bienvenidas al sistema de turnos de Caotica"}



