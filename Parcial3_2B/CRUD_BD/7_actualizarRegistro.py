from conexionBD import *
try:
      micursor=conexion.cursor()
      sql="update clientes2 set direccion='5 de febrero' where id=1"
      micursor.execute(sql)
      conexion.commit()
except:
    print("hubo un error fatal")
else:
   print("Dato modificado exitosamnete")
