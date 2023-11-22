
class Espada:
    def __init__(self, daño, x, y):
        self.daño = daño
        self.x = x
        self.y = y

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

class Personaje:
    def __init__(self, raza, fuerza, velocidad, agilidad, sigilo, vida, x, y):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida
        self.x = x
        self.y = y

    def movimiento(self, direccion):
        if direccion == "arriba":
            self.y += self.velocidad
        elif direccion == "abajo":
            self.y -= self.velocidad
        elif direccion == "izquierda":
            self.x -= self.velocidad
        elif direccion == "derecha":
            self.x += self.velocidad

    def equipar_espada(self, espada):
        self.espada = espada

    def atacar_dragon(self, dragon):
        if hasattr(self, 'espada'):
            danio_total = self.fuerza + self.espada.daño
            dragon.vida -= danio_total
        else:
            print("No tienes una espada equipada.")

obj1 = Personaje("Elfo", 150, 200, 800, 400, 800, 0, 0)
obj2 = Personaje("Dragon", 300, 200, 100, 100, 1000, 5, 5)
obj3 = Espada(500, 2, 2)


print("Elija su desicion:")
desición = int(input("--> "))




