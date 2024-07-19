from conexionBD import *

micursor=conexion.cursor()
sql='select * from clientes2'
micursor.execute(sql)
resultado=micursor.fetchall()

for x in resultado:
    print(x)
