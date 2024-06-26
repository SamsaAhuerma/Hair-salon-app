def servisEntity(item)->dict:
    return{
        "id":str(item["_id"]),
        "servis_name":item["servis_name"],
        "servis_description":item["servis_description"],
        "servis_duration":item["servis_duration"],
        "servis_price":item["servis_price"]       
    }

def servicesEntity(services)->list:
    return [servisEntity(servis) for servis in services]