class Enemigo:
    def __init__(self, raza, fuerza, velocidad, agilidad, sigilo, vida, x, y, nombre):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida
        self.nombre = nombre
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

    def atacar(self, objetivo):
        danio_total = self.fuerza
        objetivo.vida -= danio_total
        print(f"{self.raza} atacó a {objetivo.raza} con un daño de {danio_total}")