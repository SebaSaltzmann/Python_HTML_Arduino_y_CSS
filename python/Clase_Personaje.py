class Personaje:
    def __init__(self, raza, fuerza, velocidad, agilidad, sigilo, vida, x, y, nombre):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida
        self.x = x
        self.y = y
        self.espada = None
        self.nombre = nombre
    
    def equipar_espada(self, espada):
        self.espada = espada

    def movimiento(self):
        menu = """ingrese a que direccion quiere ir:
            opciones :
            ####-arriba ######
            ####-abajo #######
            ####-izquierda ###
            ####-derecha ##### """
        print(menu)
        
        direccion = (input("--> "))
        
        if direccion == "arriba":
            self.y += 1
        elif direccion == "abajo":
            self.y -= 1
        elif direccion == "izquierda":
            self.x -= 1
        elif direccion == "derecha":
            self.x += 1

    def asignar_nombre(self):
        self.nombre = (input("ingrese el nombre de su espada: "))
        return self.nombre