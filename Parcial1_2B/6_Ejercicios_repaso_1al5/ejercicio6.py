def print_tabla(n):
    print(f"La tabla es del numero {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

for j in range(1, 11):
    print_tabla(j)
    print()  