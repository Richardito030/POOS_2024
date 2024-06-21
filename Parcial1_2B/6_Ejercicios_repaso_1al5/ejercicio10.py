cantidad_alumnos =15
aprobados = 0
reprobados = 0

for i in range(cantidad_alumnos):
    calificacion = float(input(f"Escribe calificación del alumno {i+1}: "))
    if calificacion <=5:
        reprobados += 1
    else:
        aprobados += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
