
words = []
if not words:
    print("La lista está vacía. Añade tu frase,escribe end para finalizar:")
    while True:
        word = input("Añadir frase: ")
        if word.lower() == 'end':
            break
        words.append(word)

print("\nContenido de la lista en mayúsculas:")
for word in words:
    print(word.upper())
