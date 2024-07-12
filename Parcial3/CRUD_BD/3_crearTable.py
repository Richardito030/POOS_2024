from conexionBD import *
try:
  micursor=conexion.is_connected()
  sql="create table clientes2(id init primary key auto_increment,nombre varchar(60), direccion varchar(100),tel varchar(10))"
  micursor.execute.sql()
except:
 print("ocurrio un error")
else :
 print("se creo tabla exitosamente")
#micursor=conexion.cursor()
#if micursor:
 #   print("se creo la tabla exitosamente")





