
import psycopg2 

conexion=psycopg2.connect(user='postgres',
                        password='admin',
                        host='localhost',
                        port='5432',
                        database='db_consecionario')   

cursor=conexion.cursor()
sql='SELECT * FROM consecionario'

cursor.execute(sql)

registro=cursor.fetchall()
print(registro)

cursor.close()
conexion.close()