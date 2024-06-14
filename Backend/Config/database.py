import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='password',
        database='bd_pruebas'
    )

    print("Conexión exitosa")

except Exception as ex:
    print(ex)