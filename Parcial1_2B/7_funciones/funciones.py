
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#    1.- Funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
   nombre=input("Ingresa el nombre completo: ")


#Ejemplo 2 sumar dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

#Ejemplo 3 sumar dos numeros 
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros 
# 3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros 
# 4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")


#Ejemplo 5 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del Paciente, Edad, Estatura, Tipo de Sangre. Utilizar los 4 tipos de funciones

def print_welcome_message():
    print("Bienvenido al sistema de registro de pacientes")

def print_patient_info(nombre, edad, estatura, tipo_sangre):
    print(f"Nombre del Paciente: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Estatura: {estatura} metros")
    print(f"Tipo de Sangre: {tipo_sangre}")

def get_patient_info():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    return nombre, edad, estatura, tipo_sangre

def create_patient_dict(nombre, edad, estatura, tipo_sangre):
    return {
        "Nombre": nombre,
        "Edad": edad,
        "Estatura": estatura,
        "Tipo de Sangre": tipo_sangre
    }

print_welcome_message()
nombre, edad, estatura, tipo_sangre = get_patient_info()
print_patient_info(nombre, edad, estatura, tipo_sangre)
diccionario_paciente = create_patient_dict(nombre, edad, estatura, tipo_sangre)
print("Información del paciente almacenada en un diccionario:", diccionario_paciente)
