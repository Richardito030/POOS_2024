class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_info(self):
        return f"Nombre del usuario: {self.nombre}, Dirección de su casa: {self.direccion}, Teléfono celular: {self.telefono}"

class Cliente(Usuario):
    def __init__(self, nombre, direccion, telefono, num_cliente):
        super().__init__(nombre, direccion, telefono)
        self.num_cliente = num_cliente

    def mostrar_info(self):
        info_usuario = super().mostrar_info()
        return f"{info_usuario}, Número de Cliente: {self.num_cliente}"

class Empleado(Usuario):
    def __init__(self, nombre, direccion, telefono, salario, numero_empleado, tipo):
        super().__init__(nombre, direccion, telefono)
        self.salario = salario
        self.numero_empleado = numero_empleado
        self.tipo = tipo

    def mostrar_info(self):
        info_usuario = super().mostrar_info()
        return f"{info_usuario}, Salario: {self.salario}, Empleados: {self.numero_empleado}"

