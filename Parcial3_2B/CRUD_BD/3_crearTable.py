from conexionBD import conexion

try:
    if conexion.is_connected():
        micursor = conexion.cursor()
        sql = '''
        CREATE TABLE clientes2 (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(60),
            direccion VARCHAR(100),
            tel VARCHAR(10)
        )
        '''
        micursor.execute(sql)
        conexion.commit()
        print("Se creó la tabla exitosamente")
    else:
        print("No se pudo conectar a la base de datos")
except Exception as e:
    print("Ocurrió un error:", e)
finally:
    if micursor:
        micursor.close()
    if conexion.is_connected():
        conexion.close()



