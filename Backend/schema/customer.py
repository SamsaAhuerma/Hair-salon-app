def customerEntity(item)->dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "phone":item["phone"],
        "appointments":item["appointments"]
    }