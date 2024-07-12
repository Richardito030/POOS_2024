from conexionBD import *
try:
   micursor=conexion.cursor()
   nombre=input("cual es tu nombre:")
   direccion=input("escriube tu direccion:")
   tel=input("Cual es tu numero de telefono:")
   sql="INSERT INTO clientes (id,nombre,direccion,tel) values (null,%s,%s,%s)"
   micursor.execute(sql)
   #sirve para finalizar la ejecución de SQL
   conexion.commit()
except:
   print(f"hubo un error al subir los datos")
else:
   print(f"registro insertado exitosamente")