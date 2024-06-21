n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones básicas
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
if n2 != 0:
    division = n1 / n2
else:
    division = "Error: División por cero no permitida"


print(f"El resultado de la suma es: {n1} + {n2} = {suma}")
print(f"El resultado de la resta es: {n1} - {n2} = {resta}")
print(f"El resultado de la multiplicasion es: {n1} * {n2} = {multiplicacion}")
print(f"El resultado de la division es: {n1} / {n2} = {division}")

