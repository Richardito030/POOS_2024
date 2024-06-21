#Bucle while
print("Cuadrados de los 60 números naturales (while):")
n = 1
while n <= 60:
    cuadrado = n * n
    print(f"{n}^2 = {cuadrado}")
    n += 1

#Bucle for
print("Cuadrados de los 60 números naturales (for):")
for n in range(1, 61):
    cuadrado = n * n
    print(f"{n}^2 = {cuadrado}")
