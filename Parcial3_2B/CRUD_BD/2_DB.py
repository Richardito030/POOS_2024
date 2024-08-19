import mysql.connector

conexion = None

try:
    # Conectar sin especificar la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    micursor = conexion.cursor()

    # Crear la base de datos si no existe
    sql = "CREATE DATABASE IF NOT EXISTS db_python"
    micursor.execute(sql)
    
    # Seleccionar la base de datos
    conexion.database = 'db_python'
    
    # Mostrar las bases de datos que existen en el servidor MYSQL
    micursor.execute("SHOW DATABASES")
    
    for x in micursor:
        print(x)
        
    print("Se creó la base de datos exitosamente")

except mysql.connector.Error as err:
    print(f"Ocurrió un error con el sistema de verificación: {err}")

finally:
    if conexion and conexion.is_connected():
        micursor.close()
        conexion.close()
