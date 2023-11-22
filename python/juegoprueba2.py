import random

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
        self.espada = None

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

    def atacar(self, objetivo):
        if self.espada is not None:
            danio_total = self.fuerza + self.espada.daño
            objetivo.vida -= danio_total
        else:
            print("No tienes una espada equipada.")

# Crear objetos
obj1 = Personaje("Elfo", 150, 200, 800, 400, 800, 0, 0)
obj2 = Personaje("Dragon", 300, 200, 100, 100, 1000, 5, 5)
obj3 = Espada(500, 2, 2)

# Verificar colisión entre el personaje y la espada
if (
    obj1.x == obj3.x and
    obj1.y == obj3.y
):
    print("¡Colisión! El personaje ha recogido la espada.")
    obj1.equipar_espada(obj3)

# Realizar un ataque
if obj1.espada is not None:
    obj1.atacar(obj3)
    print(f"La espada ha infligido {obj3.daño} de daño al objetivo.")
