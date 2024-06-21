paises= ["Australia","Mexico","Brasil","Japon"]
numeros= [23,34,66.56,0.100]
texto= ["Cars","True",23,3.141567]

#ordenar lista
print(paises)
paises.sort()
print(paises)
#ordenar nuemrios
print(numeros)
numeros.sort()
print(numeros)
#anadir elementos
print(texto)
texto.insert(len(texto),"true")
print(texto)
texto.insert(len(texto),False)
print(texto)
texto.append(False)
print(texto)
#eliminar elementos
print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)
print(numeros)
#dar vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)
#numeros 
#buscar dato dentro de una lista
respuesta="brasil" in paises
print(respuesta)

#cuantas veces aparece un valor dentro de una lista
print(numeros)
numeros.append(23)
cuantos=numeros.count(23)
print("nuemros encontrados{cuantos}")
#unir listas 
int(paises)
