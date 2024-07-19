from conexionBD import conexion  

try:
    if conexion.is_connected():
        micursor = conexion.cursor()

        nombre = input("Escribe el nombre: ")
        direccion = input("Escribe tu dirección: ")
        tel = input("Escribe tu numero telefonico:")

        sql = "INSERT INTO clientes2 (nombre, direccion, tel) VALUES (%s, %s, %s)"
        micursor.execute(sql, (nombre, direccion, tel))

        conexion.commit()
        print("Registro insertado exitosamente")
    else:
        print("No se pudo conectar a la base de datos")
except Exception as e:
    print(f"Hubo un error al subir los datos: {e}")
finally:
    if micursor:
        micursor.close()
    if conexion.is_connected():
        conexion.close()
