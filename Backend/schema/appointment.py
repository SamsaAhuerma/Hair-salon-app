def appointmentEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "customer_id": item["customer_id"],
        "service_id": item["service_id"],
        "time": item["time"],
        "date": item["date"],
        "message": item["message"]
    }

def appointmentsEntity(appointments) -> list:
    return [appointmentEntity(appointment) for appointment in appointments]
