movies_list = [
    {"ACCION": "MAXIMA VELOCIDAD", "TERROR": "LA MONJA", "DEPORTES": "ESPN"},
    {"ACCION": "ARMA MORTAL 4", "TERROR": "EL CONJURO", "DEPORTES": "MAS DEPORTE"},
    {"ACCION": "RAPIDO Y FURIOSO I", "TERROR": "LA MALDICION", "DEPORTES": "ACCION"}
]


print("Lista de películas:")
for movie in movies_list:
    print(f"ACCION: {movie['ACCION']}, TERROR: {movie['TERROR']}, DEPORTES: {movie['DEPORTES']}")
