class Espada:
    def __init__(self, daño, nombre, x, y):
        self.daño = daño
        self.x = x
        self.y = y
        self.nombre = nombre

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

    def asignar_nombre(self):
        self.nombre = (input("ingrese el nombre de su espada: "))
        return self.nombre