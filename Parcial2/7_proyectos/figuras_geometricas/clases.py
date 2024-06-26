import math

class Figuras:
    def __init__(self, x, y, visible1=True):
        self.x = x
        self.y = y
        self.visible = visible1

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
#-------------------------------------------------------------------------------------------------------------
    def calculararea(self):
        pass 

class Rectangulo(Figuras):
    def __init__(self, x, y, alto, ancho):
        super().__init__(x, y)
        self.alto = alto
        self.ancho = ancho

    def calculararea(self):
        return self.alto * self.ancho

class Circulo(Figuras):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = radio

    def calculararea(self):
        return math.pi * (self.radio ** 2)



