# main.py
import os
import Calculadora_basica
from gestor_peliculas import add_movie, remove_movie, update_movie, list_movies, clear_movies
def main():
    print("Calculadora en Python")
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz Cuadrada")
    print("6. Potencia")

    operacion = input("Introduce el número de la operación: ")

    if operacion in ['1', '2', '3', '4', '6']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    
    if operacion == '1':
        print(f"Resultado: {Calculadora_basica.sumar(num1, num2)}")
    elif operacion == '2':
        print(f"Resultado: {Calculadora_basica.restar(num1, num2)}")
    elif operacion == '3':
        print(f"Resultado: {Calculadora_basica.multiplicar(num1, num2)}")
    elif operacion == '4':
        try:
            print(f"Resultado: {Calculadora_basica.dividir(num1, num2)}")
        except ValueError as e:
            print(e)
    elif operacion == '5':
        num = float(input("Introduce el número: "))
        try:
            print(f"Resultado: {Calculadora_basica.raiz_cuadrada(num)}")
        except ValueError as e:
            print(e)
    elif operacion == '6':
        print(f"Resultado: {Calculadora_basica.potencia(num1, num2)}")
    else:
        print("Operación no válida")

if __name__ == "__main__":
    main()

##########################################################################
# main.py

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- Gestión de Películas ---")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas de la taquilla")
    print("4. Actualizar nombre de película")
    print("5. Vaciar lista de películas")
    print("6. Salir")

def gestionar_peliculas():
    """Función principal para gestionar el menú y las opciones del usuario."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción válida: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la película: ")
            add_movie(nombre)
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la película que desea quitar: ")
            remove_movie(nombre)
        elif opcion == '3':
            list_movies()
        elif opcion == '4':
            old_name = input("Ingrese el nombre de la película que desea actualizar: ")
            new_name = input("Ingrese el nuevo nombre de la película: ")
            update_movie(old_name, new_name)
        elif opcion == '5':
            clear_movies()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la gestión de películas
if __name__ == "__main__":
    gestionar_peliculas()
