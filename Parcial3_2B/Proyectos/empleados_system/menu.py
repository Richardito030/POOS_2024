from main import Empleado

while True:
        print("Menú de opciones:")
        print("1. Agregar empleado")
        print("2. Actualizar empleado")
        print("3. Eliminar empleado")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")
#opcion 4 salir
        if opcion == '4':
            print("Saliendo del programa.")
            break
#opcion 1 crear
        elif opcion == '1':
            id_empleados = input("Ingresa el ID del empleado: ")
            nombre = input("Ingresa el nombre del empleado: ")
            puesto = input("Ingresa el puesto del empleado: ")
            salario = input("Ingresa el salario del empleado: ")
            
            nuevo_empleado = Empleado(id_empleados, nombre, puesto, salario)
            if nuevo_empleado.crear():
                print("Empleado creado exitosamente.")
            else:
                print("Error al intentar crear el empleado.")
#opcion 2 actualizar
        elif opcion == '2':
            id = input("Ingrese el ID del empleado a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            puesto = input("Ingrese el nuevo puesto del empleado: ")
            salario = input("Ingrese el nuevo salario del empleado: ")
            
            if Empleado.actualizar(id, nombre, puesto, salario):
                print("Empleado actualizado exitosamente.")
            else:
                print("Error al actualizar el empleado.")
#opcion 3 eliminar
        elif opcion == '3':
            id = input("Ingrese el ID del empleado a eliminar: ")
            
            if Empleado.eliminar(id):
                print("Empleado eliminado exitosamente.")
            else:
                print("Error al eliminar el empleado.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

