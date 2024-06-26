import math

class Figura:
    def CalcularArea(self):
        raise NotImplementedError("Debe implementar el método CalcularArea en las subclases")

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def CalcularArea(self):
        return self.largo * self.ancho

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def CalcularArea(self):
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def CalcularArea(self):
        return 0.5 * self.altura * self.ancho

# Ejemplo de uso
rectangulo = Rectangulo(5, 3)
print(f"Área del rectángulo: {rectangulo.CalcularArea()}")

circulo = Circulo(4)
print(f"Área del círculo: {circulo.CalcularArea()}")

triangulo = Triangulo(6, 4)
print(f"Área del triángulo: {triangulo.CalcularArea()}")
import math


