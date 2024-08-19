import mysql.connector
conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas'
    )
cursor=conexion.cursor(buffered=True)
class Empleado:
    def __init__(self, id_empleados, nombre, puesto, salario):
        self.id_empleados = id_empleados
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def crear(self):
        try:
            cursor.execute(
                "INSERT INTO empleados (id_empleados, Nombre, Puesto, Salario) VALUES (%s, %s, %s, %s)",
                (self.id_empleados, self.nombre, self.puesto, self.salario)
            )
            conexion.commit()
            return True
        except:
            return False   

    @staticmethod
    def mostrar(id_empleados):
        try:
            cursor.execute(
                "SELECT * FROM empleados WHERE id_empleados = %s",
                (id_empleados,)
            )
            return cursor.fetchall()
        except:
            return None    

    @staticmethod
    def actualizar(id, nombre, puesto, salario):
        try:
            cursor.execute(
                "UPDATE empleados SET Nombre=%s, Puesto=%s, Salario=%s WHERE ID=%s",
                (nombre, puesto, salario, id)
            )
            conexion.commit()
            return True
        except:
            return False  

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "DELETE FROM empleados WHERE ID=%s",
                (id,)
            )
            conexion.commit()
            return True
        except:
            return False  



