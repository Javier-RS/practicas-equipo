import psycopg2 

conexion=psycopg2.connect(user='postgres',
                        password='admin',
                        host='localhost',
                        port='5432',
                        database='db_consecionario')   

cursor=conexion.cursor()

sql='INSERT INTO consecionario(id, ubicacion, nombre) VALUES(%s,%s,%s)'

id=input('ingrese id ')
ubicacion=input('ingrese ubicacion ')
nombre=input('Ingrese nombre ')

datos=(id, ubicacion, nombre)
cursor.execute(sql,datos)
conexion.commit()
registros=cursor.rowcount

print(f'registro insertado {registros}')
cursor.close()
conexion.close()