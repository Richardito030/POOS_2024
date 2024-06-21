n1 = int(input("Inserte el primer número: "))
n2 = int(input("Inserte el segundo número: "))

if n1 > n2:
    n1, n2 = n2, n1
    
print(f"Los numeros entre {n1} y {n2} son:")
for numero in range(n1 + 1, n2):
    print(numero)
