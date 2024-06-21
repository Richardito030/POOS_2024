numbers = [34, 7, 23, 32, 5, 62, 20, 15]

print("Lista original:")
for number in numbers:
    print(number)

def recorrer_lista(lst):
    return ', '.join(str(num) for num in lst)

list_as_string = recorrer_lista(numbers)
print("\nLista como string:")
print(list_as_string)

sorted_numbers = sorted(numbers)
print("\nLista ordenada:")
for number in sorted_numbers:
    print(number)

print("\nLongitud de la lista:")
print(len(numbers))

element_to_search = int(input("\nIntroduce un número para buscar en la lista: "))

if element_to_search in numbers:
    print(f"El número {element_to_search} se encuentra en la lista.")
else:
    print(f"El número {element_to_search} no se encuentra en la lista.")
