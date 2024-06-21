#ejemplo 5 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas. 
#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas
# main.py
# gestor_peliculas.py

# Lista para almacenar los nombres de las películas
# gestor_peliculas.py

# Lista para almacenar los nombres de las películas
# gestor_peliculas.py

peliculas = ["Caroline", "Cars", "Avatar", "Rapidos y furiosos", "Transformers"]

def add_movie(nombre):
    """Agrega una película a la lista."""
    peliculas.append(nombre)
    print(f'Película "{nombre}" agregada.')

def remove_movie(nombre):
    """Remueve una película de la lista."""
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f'Película "{nombre}" removida.')
    else:
        print(f'Película "{nombre}" no encontrada.')

def update_movie(old_name, new_name):
    """Actualiza el nombre de una película en la lista."""
    if old_name in peliculas:
        index = peliculas.index(old_name)
        peliculas[index] = new_name
        print(f'Película "{old_name}" actualizada a "{new_name}".')
    else:
        print(f'Película "{old_name}" no encontrada.')

def list_movies():
    """Consulta y muestra todas las películas en la lista."""
    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print(f'- {pelicula}')
    else:
        print("No hay películas en la lista.")

def clear_movies():
    """Elimina todas las películas de la lista."""
    peliculas.clear()
    print("Todas las películas han sido eliminadas de la lista.")

