n1 = int(input("Escribe el primer número: "))
n2 = int(input("Escribe el segundo número: "))


print("Los numeros impares que podemos encontrar entre", n1, "y", n2, "son:")
for numeros in range(n1, n2 + 1):
    if numeros % 2 != 0:
        print(numeros)
