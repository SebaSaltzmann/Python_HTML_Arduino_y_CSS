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
    
    def equipar_espada(self, espada):
        self.espada = espada

    def movimiento(self, direccion):
        direccion = (input("ingrese a que direccion quiere ir: "))
        print(""" opciones :
        -arriba
        -abajo
        -izquierda
        -derecha """)

        if direccion == "arriba":
            self.y += self.velocidad
        elif direccion == "abajo":
            self.y -= self.velocidad
        elif direccion == "izquierda":
            self.x -= self.velocidad
        elif direccion == "derecha":
            self.x += self.velocidad




