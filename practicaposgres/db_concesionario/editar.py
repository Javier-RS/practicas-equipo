import psycopg2 

conexion=psycopg2.connect(user='postgres',
                        password='admin',
                        host='localhost',
                        port='5432',
                        database='db_consecionario')   

cursor=conexion.cursor()
sql='UPDATE consecionario SET id=%s, ubicacion=%s, nombre=%s WHERE id=%s'

id=input('Ingrese el id ')
ubicacion=input('Ingrese el ubicacion ')
nombre=input('Ingrese el nombre ')

datos=(id,ubicacion,nombre)
cursor.execute(sql,datos)
conexion.commit()
registro_actualizado=cursor.rowcount

print(f'registro actualizado {registro_actualizado}')

cursor.close()
conexion.close()