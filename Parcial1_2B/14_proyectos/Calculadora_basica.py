import os

#from variasfunciones import *

# def solicitarDatos():
#    global n1,n2
#    n1=int(input("Numero #1: "))
#    n2=int(input("Numero #2: "))
  

# def getCalculadora(num1,num2,operacion):
#     if operacion=="1" or operacion=="+" or operacion=="SUMA":
#         return f"{num1}+{num2}={int(num1)+int(num2)}"
#     elif operacion=="2" or operacion=="-" or operacion=="RESTA":
#         return f"{num1}-{num2}={int(num1)-int(num2)}"  
#     elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
#         return f"{num1}*{num2}={int(num1)*int(num2)}"        
#     elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
#         return f"{num1}/{num2}={int(num1)/int(num2)}"  
#     else:
#         return "Opción invalida por favor vuelve a intentarlo"        
    
# def esperaTecla():
#    # Muestra un mensaje
#    print("Presiona cualquier tecla para continuar...")

#    # Espera a que el usuario presione una tecla
#    input()


# calculadora.py

import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(a)

def potencia(a, b):
    return a ** b
