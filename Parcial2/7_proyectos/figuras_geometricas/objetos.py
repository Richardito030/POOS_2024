from clases import *

rectangulo1 = Rectangulo(x=0, y=0, alto=3, ancho=4)
print(f"Área obtenida del rectangulo: {rectangulo1.calculararea()}")

circulo1 = Circulo(x=3, y=3, radio=6)
print(f"Área obtenida círculo: {circulo1.calculararea()}")

print(f"La figura es visible: {rectangulo1.estaVisible()}")