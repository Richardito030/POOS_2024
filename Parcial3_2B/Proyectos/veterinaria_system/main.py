import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_veterinaria"
)

cursor = conexion.cursor()

while True:
    print("Menú de opciones:")
    print("1. Veterinaria")
    print("2. Confirmar Citas")
    print("3. Actualizar Servicios")
    print("4. Eliminar Clientes")
    print("5. Personas")
    print("6. Animales")
    print("7. Consultas")
    print("8. Vacunas")
    print("9. Salir")

    opcion = input("Seleccione una opción (1-9): ")

    if opcion == '9':
        print("Saliendo del programa.")
        break
    elif opcion == '1':
        print("Opciones de Veterinaria:")
        print("1. Agregar cliente")
        print("2. Agregar empleado")
        print("3. Agregar cita")
        print("4. Agregar servicio")
        subopcion = input("Seleccione una opción (1-4): ")
        
        if subopcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            animal = input("Ingrese el tipo de animal: ")
            tipo = input("Ingrese el tipo de animal: ")
            
            query = "INSERT INTO clientes (Nombre, Animal, Tipo) VALUES (%s, %s, %s)"
            valores = (nombre, animal, tipo)
            cursor.execute(query, valores)
            conexion.commit()
            print("Cliente agregado exitosamente.")
        elif subopcion == '2':
            nombre = input("Ingrese el nombre del empleado: ")
            puesto = input("Ingrese el puesto del empleado: ")
            salario = input("Ingrese el salario del empleado: ")
            
            query = "INSERT INTO empleados (Nombre, Puesto, Salario) VALUES (%s, %s, %s)"
            valores = (nombre, puesto, salario)
            cursor.execute(query, valores)
            conexion.commit()
            print("Empleado agregado exitosamente.")
        elif subopcion == '3':
            duracion = input("Ingrese la duración de la cita: ")
            fecha = input("Ingrese la fecha de la cita: ")
            
            query = "INSERT INTO citas (Duracion, Fecha) VALUES (%s, %s)"
            valores = (duracion, fecha)
            cursor.execute(query, valores)
            conexion.commit()
            print("Cita agregada exitosamente.")
        elif subopcion == '4':
            nombre = input("Ingrese el nombre del servicio: ")
            descripcion = input("Ingrese la descripción del servicio: ")
            costo = input("Ingrese el costo del servicio: ")
            
            query = "INSERT INTO servicios (Nombre, Descripcion, Costo) VALUES (%s, %s, %s)"
            valores = (nombre, descripcion, costo)
            cursor.execute(query, valores)
            conexion.commit()
            print("Servicio agregado exitosamente.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
    elif opcion == '2':
        print("Confirmar Cita:")
        fecha = input("Ingrese la fecha de la cita: ")
        id_cliente = input("Ingrese el ID del cliente: ")
        id_animal = input("Ingrese el ID del animal: ")
        id_empleado = input("Ingrese el ID del empleado: ")
        id_servicio = input("Ingrese el ID del servicio: ")
        
        # Validar que todos los IDs existan en sus respectivas tablas
        cursor.execute("SELECT COUNT(*) FROM clientes WHERE id_clientes = %s", (id_cliente,))
        cliente_existe = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM animales WHERE id_animales = %s", (id_animal,))
        animal_existe = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM empleados WHERE id_empleados = %s", (id_empleado,))
        empleado_existe = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM servicios WHERE id_servicios = %s", (id_servicio,))
        servicio_existe = cursor.fetchone()[0]
        
        if cliente_existe and animal_existe and empleado_existe and servicio_existe:
            confirmar = input("¿Desea confirmar la cita? (si/no): ")
            if confirmar.lower() == 'si':
                print("Cita confirmada exitosamente.")
            else:
                print("Cita no confirmada.")
        else:
            print("Error: Uno o más IDs no existen.")
    elif opcion == '3':
        print("Actualizar Servicio:")
        id_servicio = input("Ingrese el ID del servicio a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del servicio: ")
        descripcion = input("Ingrese la nueva descripción del servicio: ")
        costo = input("Ingrese el nuevo costo del servicio: ")
        
        query = "UPDATE servicios SET Nombre = %s, Descripcion = %s, Costo = %s WHERE id_servicios = %s"
        valores = (nombre, descripcion, costo, id_servicio)
        cursor.execute(query, valores)
        conexion.commit()
        print("Servicio actualizado exitosamente.")
    elif opcion == '4':
        print("Eliminar Cliente:")
        id_cliente = input("Ingrese el ID del cliente a eliminar: ")
        
        query = "DELETE FROM clientes WHERE id_clientes = %s"
        valores = (id_cliente,)
        cursor.execute(query, valores)
        conexion.commit()
        print("Cliente eliminado exitosamente.")
    elif opcion == '5':
        print("Opciones de Personas:")
        print("1. Agregar persona")
        print("2. Actualizar persona")
        subopcion = input("Seleccione una opción (1-2): ")
        
        if subopcion == '1':
            nombre = input("Ingrese el nombre de la persona: ")
            direccion = input("Ingrese la dirección de la persona: ")
            telefono = input("Ingrese el teléfono de la persona: ")
            
            query = "INSERT INTO personas (Nombre, Direccion, Telefono) VALUES (%s, %s, %s)"
            valores = (nombre, direccion, telefono)
            cursor.execute(query, valores)
            conexion.commit()
            print("Persona agregada exitosamente.")
        elif subopcion == '2':
            id_persona = input("Ingrese el ID de la persona a actualizar: ")
            nombre = input("Ingrese el nuevo nombre de la persona: ")
            direccion = input("Ingrese la nueva dirección de la persona: ")
            telefono = input("Ingrese el nuevo teléfono de la persona: ")
            
            query = "UPDATE personas SET Nombre = %s, Direccion = %s, Telefono = %s WHERE id_personas = %s"
            valores = (nombre, direccion, telefono, id_persona)
            cursor.execute(query, valores)
            conexion.commit()
            print("Persona actualizada exitosamente.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
    elif opcion == '6':
        print("Opciones de Animales:")
        print("1. Agregar animal")
        print("2. Actualizar animal")
        subopcion = input("Seleccione una opción (1-2): ")
        
        if subopcion == '1':
            nombre = input("Ingrese el nombre del animal: ")
            raza = input("Ingrese la raza del animal: ")
            edad = input("Ingrese la edad del animal: ")
            
            query = "INSERT INTO animales (Nombre, Raza, Edad) VALUES (%s, %s, %s)"
            valores = (nombre, raza, edad)
            cursor.execute(query, valores)
            conexion.commit()
            print("Animal agregado exitosamente.")
        elif subopcion == '2':
            id_animal = input("Ingrese el ID del animal a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del animal: ")
            raza = input("Ingrese la nueva raza del animal: ")
            edad = input("Ingrese la nueva edad del animal: ")
            
            query = "UPDATE animales SET Nombre = %s, Raza = %s, Edad = %s WHERE id_animales = %s"
            valores = (nombre, raza, edad, id_animal)
            cursor.execute(query, valores)
            conexion.commit()
            print("Animal actualizado exitosamente.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
    elif opcion == '7':
        print("Agregar Consulta:")
        duracion = input("Ingrese la duración de la consulta: ")
        fecha = input("Ingrese la fecha de la consulta: ")
        
        query = "INSERT INTO consultas (Duracion, Fecha) VALUES (%s, %s)"
        valores = (duracion, fecha)
        cursor.execute(query, valores)
        conexion.commit()
        print("Consulta agregada exitosamente.")
    elif opcion == '8':
        print("Opciones de Vacunas:")
        print("1. Agregar vacuna")
        print("2. Administrar vacuna")
        subopcion = input("Seleccione una opción (1-2): ")
        
        if subopcion == '1':
            tipo = input("Ingrese el tipo de vacuna: ")
            query = "INSERT INTO vacunas (tipo) VALUES (%s)"
            valores = (tipo,)
            cursor.execute(query, valores)
            conexion.commit()
            print("Tipo de vacuna agregado exitosamente.")
        elif subopcion == '2':
            tipo_vacuna = input("Ingrese el tipo de vacuna a administrar: ")
            print("Vacuna administrada: " + tipo_vacuna)
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")

cursor.close()
conexion.close()
