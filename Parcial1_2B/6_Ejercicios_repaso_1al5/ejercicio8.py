def calcular_porcentaje(n, porcentaje):
    r = (porcentaje / 100) * n
    return r

n = float(input("Escribe el número: "))
porcentaje = float(input("Escribe el porcentaje de un numero (no uses %): "))

resultado_porcentaje = calcular_porcentaje(n, porcentaje)

print(f"El {porcentaje}% de {n} es: {resultado_porcentaje}")
