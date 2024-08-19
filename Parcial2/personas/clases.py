class Personas:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Dirección : {self.edad}, Teléfono: {self.telefono}")
personas=Personas("Daniel",20,"618-278-8938")
personas.mostrar_info()

def getNombre(self):
    return self.nombre

def getEdad(self):
    return self.edad

def getTelefono(self):
    return self.telefono

def setNombre(self):
    return self.edad

def setEdad(self):
    return self.edad

def setTelefono(self):
    return self.telefono

class Estudiantes(Personas):
  def __init__(self, nombre, edad, telefono, carrera, matricula):
         super().__init__(nombre, edad, telefono)
         self.carrera=carrera
         self.matricula=matricula

def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Dirección : {self.edad}, Teléfono: {self.telefono},Carrera:{self.carrera},matriucla:{self.matricula}")
personas=Personas("Daniel",20,"618-278-8938","programacion",23456)

def getCarrera(self):
    return self.carrera

def getMatricula(self):
    return self.matricula

def setCarrera(self):
    return self.carrera

def setMatricula(self):
    return self.matricula

class Docentes(Personas):
 def __init__(self, nombre, edad, telefono):
         super().__init__(nombre, edad, telefono)
         self.carrera=carrera
         self.matricula=matricula