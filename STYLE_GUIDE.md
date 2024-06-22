# Comunicación con la base de datos
`nameClass`ComunicationDB

# Nombre de funciones que se comuniquen con la DB
Al importar una colleción le ponemos etiqueta `db`
```python
from config.database import customer_collection as db
```

```python
def create_nameclass():

def get_nameclass_by_id():

def get_list_of_nameclass():

def update_nameclass_by_id(): 

def delete_nameclass_by_id()
```

# Manejo de excepciones con DB
```python
fom pymongo.errors import WTimeoutError
exception WTimeoutError --> la consutla
exception PyMongoError
```
Ejemplo de funcion de la comunicación con la DB
Debe manejar el PyMongoError y el WTimeoutError
todas las funciones deben devolver la respuesta con la db
```python
def get_list_of_customers():
        try:
            customers = bd.find()
            return customers
        except WTimeoutError:
            return {"error":"Timeout expired... query error"}
        except PyMongoError as e:
            return {"error":str(e)}
```
# Routers
Usar prefijo, tag y respuesta por default  
Además crear una instancia de la comunicación por fuera  
Ejemplo:
```python
router = APIRouter(prefix="/servis",
                    tags=["Servis"],
                    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}},)

com_db = ServisComunicationDB()
```

## Endpoints
Nombre de las funciones:
```python
async def get_all_nameclass():

async def create_nameclass():

async def get_nameclass():

async def update_nameclass():

async def delete_nameclass():
```

Ejemplo de como debe ser una función de endpoint (ruta)
Debe estar encerrado por un try-except y el except hacer un raise de **INTERNAL SERVER ERROR**
```python
@router.post("/customers")
async def create_customer(customer : Customer):
    #falta validación de datos acá ?¿
    try:
        customer_created = customerComunicationDB.create_customer(customer)
        return customerEntity(customer_created)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server error")
```
# Schema
Nombre de los Schemas:
```python
def customerNameclass(item)->dict

#def customerNameclass(es)(nameclass(es))->list
```

Ejemplo:
```python
def customerEntity(item)->dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "phone":item["phone"],
        "appointments":item["appointments"]
    }

def customersEntity(customers)->list:
    return [customerEntity(customer) for customer in customers]
```
